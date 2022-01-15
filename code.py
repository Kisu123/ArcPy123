

import arcpy


from arcpy import env



fclayer = arcpy.GetParameterAsText(0)

fcname = arcpy.GetParameterAsText(1)

workspace = arcpy.GetParameterAsText(2)

arcpy.env.workspace = workspace

buff = arcpy.Buffer_analysis(fclayer,fcname,'1000 Meters')

