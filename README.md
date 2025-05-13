# Drogon CRONs

GitHub Action-controlled CRON jobs to run on a self-hosted runner on Drogon.

Follow instructions from settings for establishing self-hosted runner.

Find the startup script at `/home/cbaker239/startup.sh`:, which should trigger on restart of Drogon, and which should currently be:

```bash
tmux new -scodys_self_hosted_runner
cd /mnt/backup/dandi/dandiarchive-logs-cody/self_hosted_runner/actions-runner
./run.cmd
```

Which should trigger on restart of Drogon via:

```bash
crontab -e
> @reboot  /home/user/startup.sh
``
