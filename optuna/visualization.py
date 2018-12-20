from optuna.study import Study

try:
    import plotly.graph_objs as go
    from plotly.offline import iplot
    from plotly.offline import init_notebook_mode
    _available = True
except ImportError as e:
    _import_error = e
    # Visualization features are disabled because plotly is not available.
    _available = False


def plot_intermediate_values(study, filename=None, layout=None):
    # type: (Study) -> None

    """Plot intermediate values of a study.

    Example:

        .. code::
            import optuna
            from plotly.offline import init_notebook_mode

            def objective(trial):
                ...

            study = optuna.create_study()
            study.optimize(n_trials=100)

            init_notebook_mode(connected=True)
            optuna.visualization.plot_intermediate_values(study)

    """

    _check_plotly_availability()

    filename = filename or 'plot_image'
    layout = layout or {'showlegend': False}

    trials = study.trials
    intermediate_values = [t.intermediate_values for t in trials]
    intermediate_values = [iv for iv in intermediate_values if len(iv) != 0]
    data = [go.Scatter(x=list(iv.keys()), y=list(iv.values())) for iv in intermediate_values]

    iplot(go.Figure(data=data, layout=layout), filename)


def _check_plotly_availability():
    # type: () -> None

    if not _available:
        raise ImportError(
            'Plotly is not available. Please install plotly to use this feature. '
            'Plotly can be installed by executing `$ pip install plotly`. '
            'For further information, please refer to the installation guide of plotly. '
            '(The actual import error is as follows: ' + str(_import_error) + ')')
