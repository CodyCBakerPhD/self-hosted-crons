# Self-hosted CRONs

GitHub Action-controlled CRON jobs to run on a self-hosted runner on remote servers.

Follow the instructions from settings for establishing self-hosted runner.

A startup script at `~/startup.sh`:

```bash
tmux new -scodys_self_hosted_runner
cd /mnt/backup/dandi/dandiarchive-logs-cody/self_hosted_runner/actions-runner
./run.cmd
```

Which should trigger on restart via:

```bash
crontab -e
> @reboot  /home/user/startup.sh
``
