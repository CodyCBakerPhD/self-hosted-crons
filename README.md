# Self-hosted CRONs

GitHub Action-controlled CRON jobs to run on a self-hosted runner on remote servers.

Follow the instructions from settings for establishing self-hosted runner.

To restart job runner after system reboot:

```bash
tmux new -scodys_self_hosted_runner
cd /data/dandi/s3-logs/self_hosted_runner/actions-runner
./run.cmd
```
