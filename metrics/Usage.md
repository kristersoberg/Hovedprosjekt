# View full dashboard (default)
python automation/metrics_dashboard.py

# View only summary statistics
python automation/metrics_dashboard.py --summary

# View detailed statistics
python automation/metrics_dashboard.py --detailed

# View recent 20 runs
python automation/metrics_dashboard.py --recent 20

# Export to CSV for analysis in Excel/Python
python automation/metrics_dashboard.py --export metrics.csv
