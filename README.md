# Self-hosted CRONs

This repository previously held GitHub Actions CRON jobs that ran on a self-hosted runner.

Everything has since moved, and only this record of the development history remains.

| What | Where it went |
| --- | --- |
| DANDI usage workflows: log extraction, S3 Inventory sync, package install, and the Dandiset, archive, microscopy and unassociated summaries | [brain-bbqs-runners/dandi-usage-runner](https://github.com/brain-bbqs-runners/dandi-usage-runner) |
| EMBER usage workflows: log extraction, package install, and the Dandiset, archive and unassociated summaries | [brain-bbqs-runners/ember-usage-runner](https://github.com/brain-bbqs-runners/ember-usage-runner) |
| The composite actions those workflows shared, for running extraction commands, uploading summaries and installing packages | [CodyCBakerPhD/dandi-s3-logs-action](https://github.com/CodyCBakerPhD/dandi-s3-logs-action) |
| The pre-run check that the self-hosted runner is online | [CodyCBakerPhD/check-runner-action](https://github.com/CodyCBakerPhD/check-runner-action) |
