_base_ = './tt_default.py'

expname = 'dvgo_M60_unbounded'

data = dict(
    datadir='./data/tanks_and_temples/tat_intermediate_M60',
    load2gpu_on_the_fly=True,
)

