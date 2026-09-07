"""
Verify that the ``ip_to_region.yaml`` cache holds only labels of the GeoLite2 era.

Every value must be one of:

- ``<ISO 3166-1 alpha-3>`` or ``<alpha-3>/<ISO 3166-2 subdivision>``, as in ``DEU`` or ``USA/CA``
- an alpha-2 passthrough for a code outside ISO 3166-1, as in ``XK``, optionally with a subdivision
- a cloud service or VPN label, as in ``GitHub``, ``VPN``, ``AWS/us-east-1``, ``GCP/us-central1``
- ``bogon`` (a non-global address) or ``unknown`` (malformed, or absent from the database)

A ``None`` value, or an old-style label such as ``US/California``, fails the check.

Usage:
    python verify_ip_to_region.py --cache <extraction cache> [--encryption {true,false}]
"""

import argparse
import collections
import re
import sys

from s3_log_extraction.ip_utils import is_cloud_service_or_vpn_label, load_ip_cache

# Alpha-3 country code, or alpha-2 passthrough for a code outside ISO 3166-1, each with an optional subdivision
REGION_LABEL_PATTERN = re.compile(pattern=r"^[A-Z]{2,3}(/[A-Z0-9]{1,3})?$")
UNRESOLVED_LABELS = frozenset(["bogon", "unknown"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", required=True, help="Path to the extraction cache directory.")
    parser.add_argument(
        "--encryption",
        default="true",
        choices=["true", "false"],
        help="Whether the IP cache files are encrypted. Must match the pipeline setting.",
    )
    arguments = parser.parse_args()

    ip_to_region = load_ip_cache(
        cache_type="ip_to_region",
        cache_directory=arguments.cache,
        use_encryption=arguments.encryption == "true",
    )

    none_count = 0
    invalid_labels: collections.Counter[str] = collections.Counter()
    label_counts: collections.Counter[str] = collections.Counter()
    for region_label in ip_to_region.values():
        if region_label is None:
            none_count += 1
            continue
        label_counts[region_label] += 1
        if (
            region_label in UNRESOLVED_LABELS
            or is_cloud_service_or_vpn_label(region_label)
            or REGION_LABEL_PATTERN.match(string=region_label) is not None
        ):
            continue
        invalid_labels[region_label] += 1

    total = len(ip_to_region)
    print(f"Total entries: {total}")
    print(f"'unknown' labels: {label_counts['unknown']}")
    print(f"'bogon' labels: {label_counts['bogon']}")
    print(f"None values: {none_count}")
    print(f"Distinct labels: {len(label_counts)}")

    if none_count == 0 and not invalid_labels:
        print("All labels match the expected GeoLite2-era formats.")
        return 0

    if invalid_labels:
        print(f"\n{sum(invalid_labels.values())} entries carry an unexpected label; most common:")
        for region_label, count in invalid_labels.most_common(n=20):
            print(f"  {region_label}: {count}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
