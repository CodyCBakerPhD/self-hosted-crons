# Self-hosted CRONs

This repository held GitHub Action-controlled CRON jobs that ran on a self-hosted runner. Everything has
since moved, and only this record remains.

| What | Where it went |
| --- | --- |
| DANDI usage workflows: log extraction, S3 Inventory sync, package install, and the Dandiset, archive, microscopy and unassociated summaries | [brain-bbqs-runners/dandi-usage-runner](https://github.com/brain-bbqs-runners/dandi-usage-runner) |
| EMBER usage workflows: log extraction, package install, and the Dandiset, archive and unassociated summaries | [brain-bbqs-runners/ember-usage-runner](https://github.com/brain-bbqs-runners/ember-usage-runner) |
| The composite actions those workflows shared, for running extraction commands, uploading summaries and installing packages | [CodyCBakerPhD/dandi-s3-logs-action](https://github.com/CodyCBakerPhD/dandi-s3-logs-action) |
| The pre-run check that the self-hosted runner is online | [CodyCBakerPhD/check-runner-action](https://github.com/CodyCBakerPhD/check-runner-action) |

Older one-off workflows, for AIND ephys runs, DANDI compute monitoring and BIDS Dandiset updates, were deleted
before the move rather than migrated.

Everything that ran here is still in the history. [`0579614`](https://github.com/CodyCBakerPhD/self-hosted-crons/tree/05796143818e123f0e5e2c7206ce80787126fa6b)
is the last commit before the move began.
