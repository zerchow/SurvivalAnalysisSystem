from django.shortcuts import render
from django.shortcuts import render_to_response
from lifelines.datasets import load_waltons
from lifelines import KaplanMeierFitter
from lifelines import NelsonAalenFitter
import os
import matplotlib.pyplot as plt

def get_sa(request):
    dirname = os.path.dirname(os.path.dirname(__file__)).replace('\\', '/')
    kmffile = '/images/test1.jpg'
    naffile = '/images/test2.jpg'
    context = {}
    context['kmf'] = kmffile
    context['naf'] = naffile
    if not os.path.exists(dirname + kmffile) and not os.path.exists(dirname + naffile):
        df = load_waltons()
        T = df['T']  # an array of durations
        E = df['E']  # a either boolean or binary array representing whether the 'death' was observed (alternatively an individual can be censored)
        kmf = KaplanMeierFitter(alpha=0.95)
        kmf.fit(durations=T, event_observed=E, timeline=None, entry=None, label='KM_estimate', alpha=None, left_censorship=False, ci_labels=None)

        naf = NelsonAalenFitter(alpha=0.95, nelson_aalen_smoothing=True)
        naf.fit(durations=T, event_observed=E, timeline=None, entry=None, label='NA_estimate', alpha=None, ci_labels=None)

        kmf.plot()
        plt.savefig(dirname + kmffile)
        naf.plot()
        plt.savefig(dirname + naffile)

    # return render_to_response(template_name='sa_test.html', context=context, context_instance=RequestContext(request=request))
    return render(request=request, template_name='sa_test.html', context=context)