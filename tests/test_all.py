
import jikudata as jd


for dataset in jd.datasets.iter_all():
	dataset.runtest( verbose=True )

# # dataset = jd.RSWeightReduction()
# dataset = jd.Salmonella()
#
# # dataset = jd.Trees()
#
#
# print( dataset )
#
# # # print( dataset.y )
# # # print( dataset.expected )
# #
# # results = dataset.run()
# dataset.runtest( verbose=True )

