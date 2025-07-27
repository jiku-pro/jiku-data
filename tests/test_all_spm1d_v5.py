
import jikudata as jd




# def test_all():
#     for dataset in jd.datasets.iter_all():
#         if dataset._autotest:
#             if dataset.params.testname in ['ttest', 'ttest_paired', 'ttest2', 'anova1']:
#                 print( dataset.dim, dataset.name, dataset.params.testname )
#                 # dataset.runtest( verbose=True )


dataset = jd.RSFlavor()
# print( dataset )

spm     = dataset.run( spm1d_version=None )
# spm     = dataset.run( spm1d_version=4 )
# spm     = dataset.run( spm1d_version=5 )

print( spm )