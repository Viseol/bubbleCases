# trace generated using paraview version 5.11.2
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
a6mmTurOpenFOAM = FindSource('6mmTur.OpenFOAM')

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=a6mmTurOpenFOAM)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'alpha.water']
clip1.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0, 0.0, 0.05000000074505806]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.0, 0.0, 0.05000000074505806]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = [None, '']
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'U'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 0.010000000149011612
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 0.0005000000074505806
clip1Display.SetScaleArray = ['POINTS', 'U']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'U']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 0.0023104341326346937
clip1Display.OpacityArrayName = ['POINTS', 'U']
clip1Display.SelectInputVectors = ['POINTS', 'U']
clip1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide data in view
Hide(a6mmTurOpenFOAM, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(clip1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# get 2D transfer function for 'vtkBlockColors'
vtkBlockColorsTF2D = GetTransferFunction2D('vtkBlockColors')

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=clip1.ClipType)

# create a new 'Extract Time Steps'
extractTimeSteps1 = ExtractTimeSteps(registrationName='ExtractTimeSteps1', Input=clip1)
extractTimeSteps1.TimeStepIndices = [0]
extractTimeSteps1.TimeStepRange = [0, 25]

# show data in view
extractTimeSteps1Display = Show(extractTimeSteps1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractTimeSteps1Display.Representation = 'Surface'
extractTimeSteps1Display.ColorArrayName = [None, '']
extractTimeSteps1Display.SelectTCoordArray = 'None'
extractTimeSteps1Display.SelectNormalArray = 'None'
extractTimeSteps1Display.SelectTangentArray = 'None'
extractTimeSteps1Display.OSPRayScaleArray = 'U'
extractTimeSteps1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractTimeSteps1Display.SelectOrientationVectors = 'None'
extractTimeSteps1Display.ScaleFactor = 0.010000000149011612
extractTimeSteps1Display.SelectScaleArray = 'None'
extractTimeSteps1Display.GlyphType = 'Arrow'
extractTimeSteps1Display.GlyphTableIndexArray = 'None'
extractTimeSteps1Display.GaussianRadius = 0.0005000000074505806
extractTimeSteps1Display.SetScaleArray = ['POINTS', 'U']
extractTimeSteps1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractTimeSteps1Display.OpacityArray = ['POINTS', 'U']
extractTimeSteps1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractTimeSteps1Display.DataAxesGrid = 'GridAxesRepresentation'
extractTimeSteps1Display.PolarAxes = 'PolarAxesRepresentation'
extractTimeSteps1Display.ScalarOpacityUnitDistance = 0.0023104341326346937
extractTimeSteps1Display.OpacityArrayName = ['POINTS', 'U']
extractTimeSteps1Display.SelectInputVectors = ['POINTS', 'U']
extractTimeSteps1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractTimeSteps1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractTimeSteps1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(extractTimeSteps1Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
extractTimeSteps1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(extractTimeSteps1Display, ('CELLS', 'alpha.water'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
extractTimeSteps1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
extractTimeSteps1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'alphawater'
alphawaterLUT = GetColorTransferFunction('alphawater')

# get opacity transfer function/opacity map for 'alphawater'
alphawaterPWF = GetOpacityTransferFunction('alphawater')

# get 2D transfer function for 'alphawater'
alphawaterTF2D = GetTransferFunction2D('alphawater')

# Properties modified on extractTimeSteps1
extractTimeSteps1.TimeStepIndices = [1]

# update the view to ensure updated data information
renderView1.Update()

# get animation scene
animationScene1 = GetAnimationScene()

# Properties modified on animationScene1
animationScene1.AnimationTime = 0.01

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# set active source
SetActiveSource(clip1)

# create a new 'Extract Time Steps'
extractTimeSteps2 = ExtractTimeSteps(registrationName='ExtractTimeSteps2', Input=clip1)
extractTimeSteps2.TimeStepIndices = [0]
extractTimeSteps2.TimeStepRange = [0, 25]

# Properties modified on extractTimeSteps2
extractTimeSteps2.TimeStepIndices = [5]

# show data in view
extractTimeSteps2Display = Show(extractTimeSteps2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractTimeSteps2Display.Representation = 'Surface'
extractTimeSteps2Display.ColorArrayName = [None, '']
extractTimeSteps2Display.SelectTCoordArray = 'None'
extractTimeSteps2Display.SelectNormalArray = 'None'
extractTimeSteps2Display.SelectTangentArray = 'None'
extractTimeSteps2Display.OSPRayScaleArray = 'U'
extractTimeSteps2Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractTimeSteps2Display.SelectOrientationVectors = 'None'
extractTimeSteps2Display.ScaleFactor = 0.010000000149011612
extractTimeSteps2Display.SelectScaleArray = 'None'
extractTimeSteps2Display.GlyphType = 'Arrow'
extractTimeSteps2Display.GlyphTableIndexArray = 'None'
extractTimeSteps2Display.GaussianRadius = 0.0005000000074505806
extractTimeSteps2Display.SetScaleArray = ['POINTS', 'U']
extractTimeSteps2Display.ScaleTransferFunction = 'PiecewiseFunction'
extractTimeSteps2Display.OpacityArray = ['POINTS', 'U']
extractTimeSteps2Display.OpacityTransferFunction = 'PiecewiseFunction'
extractTimeSteps2Display.DataAxesGrid = 'GridAxesRepresentation'
extractTimeSteps2Display.PolarAxes = 'PolarAxesRepresentation'
extractTimeSteps2Display.ScalarOpacityUnitDistance = 0.0023104341326346937
extractTimeSteps2Display.OpacityArrayName = ['POINTS', 'U']
extractTimeSteps2Display.SelectInputVectors = ['POINTS', 'U']
extractTimeSteps2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractTimeSteps2Display.ScaleTransferFunction.Points = [-0.15456044673919678, 0.0, 0.5, 0.0, 0.18777643144130707, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractTimeSteps2Display.OpacityTransferFunction.Points = [-0.15456044673919678, 0.0, 0.5, 0.0, 0.18777643144130707, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(extractTimeSteps2Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
extractTimeSteps2Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(extractTimeSteps2, renderView1)

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=extractTimeSteps2)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['POINTS', 'alpha.water']
clip2.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [-0.014999999664723873, 0.0, 0.015]
clip2.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = [None, '']
clip2Display.SelectTCoordArray = 'None'
clip2Display.SelectNormalArray = 'None'
clip2Display.SelectTangentArray = 'None'
clip2Display.OSPRayScaleArray = 'U'
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.SelectOrientationVectors = 'None'
clip2Display.ScaleFactor = 0.00599999986588955
clip2Display.SelectScaleArray = 'None'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'None'
clip2Display.GaussianRadius = 0.00029999999329447744
clip2Display.SetScaleArray = ['POINTS', 'U']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = ['POINTS', 'U']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityUnitDistance = 0.0024378942183546507
clip2Display.OpacityArrayName = ['POINTS', 'U']
clip2Display.SelectInputVectors = ['POINTS', 'U']
clip2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display.ScaleTransferFunction.Points = [-0.0017458213260397315, 0.0, 0.5, 0.0, 0.10628702491521835, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display.OpacityTransferFunction.Points = [-0.0017458213260397315, 0.0, 0.5, 0.0, 0.10628702491521835, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractTimeSteps2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(clip2Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, True)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=clip2.ClipType)

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [-0.014999999664723873, 0.0, 0.015]
clip2.ClipType.Normal = [0.0, 0.0, -1.0]

# show data in view
clip2Display_1 = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip2Display_1.Representation = 'Surface'
clip2Display_1.ColorArrayName = [None, '']
clip2Display_1.SelectTCoordArray = 'None'
clip2Display_1.SelectNormalArray = 'None'
clip2Display_1.SelectTangentArray = 'None'
clip2Display_1.OSPRayScaleArray = 'U'
clip2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display_1.SelectOrientationVectors = 'None'
clip2Display_1.ScaleFactor = 0.008500000182539226
clip2Display_1.SelectScaleArray = 'None'
clip2Display_1.GlyphType = 'Arrow'
clip2Display_1.GlyphTableIndexArray = 'None'
clip2Display_1.GaussianRadius = 0.00042500000912696126
clip2Display_1.SetScaleArray = ['POINTS', 'U']
clip2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display_1.OpacityArray = ['POINTS', 'U']
clip2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display_1.DataAxesGrid = 'GridAxesRepresentation'
clip2Display_1.PolarAxes = 'PolarAxesRepresentation'
clip2Display_1.ScalarOpacityUnitDistance = 0.002196195727358304
clip2Display_1.OpacityArrayName = ['POINTS', 'U']
clip2Display_1.SelectInputVectors = ['POINTS', 'U']
clip2Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display_1.ScaleTransferFunction.Points = [-0.15456044673919678, 0.0, 0.5, 0.0, 0.18777643144130707, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display_1.OpacityTransferFunction.Points = [-0.15456044673919678, 0.0, 0.5, 0.0, 0.18777643144130707, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractTimeSteps2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(clip2Display_1, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
clip2Display_1.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(extractTimeSteps2)

# show data in view
extractTimeSteps2Display = Show(extractTimeSteps2, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
extractTimeSteps2Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(extractTimeSteps2, renderView1)

# set active source
SetActiveSource(clip2)

# set active source
SetActiveSource(extractTimeSteps2)

# hide data in view
Hide(clip2, renderView1)

# show data in view
extractTimeSteps2Display = Show(extractTimeSteps2, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
extractTimeSteps2Display.SetScalarBarVisibility(renderView1, True)

# destroy clip2
Delete(clip2)
del clip2

# set active source
SetActiveSource(extractTimeSteps1)

# set active source
SetActiveSource(extractTimeSteps2)

# set active source
SetActiveSource(extractTimeSteps1)

# set active source
SetActiveSource(extractTimeSteps2)

# set scalar coloring
ColorBy(extractTimeSteps2Display, ('CELLS', 'alpha.water'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
extractTimeSteps2Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
extractTimeSteps2Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=extractTimeSteps2)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['POINTS', 'alpha.water']
clip2.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=clip2.ClipType)

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [-0.014999999664723873, 0.0, 0.015]
clip2.ClipType.Normal = [1.0, 0.0, -1.0]

# show data in view
clip2Display_1 = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip2Display_1.Representation = 'Surface'
clip2Display_1.ColorArrayName = ['CELLS', 'alpha.water']
clip2Display_1.LookupTable = alphawaterLUT
clip2Display_1.SelectTCoordArray = 'None'
clip2Display_1.SelectNormalArray = 'None'
clip2Display_1.SelectTangentArray = 'None'
clip2Display_1.OSPRayScaleArray = 'U'
clip2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display_1.SelectOrientationVectors = 'None'
clip2Display_1.ScaleFactor = 0.010000000115484001
clip2Display_1.SelectScaleArray = 'None'
clip2Display_1.GlyphType = 'Arrow'
clip2Display_1.GlyphTableIndexArray = 'None'
clip2Display_1.GaussianRadius = 0.0005000000057742
clip2Display_1.SetScaleArray = ['POINTS', 'U']
clip2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display_1.OpacityArray = ['POINTS', 'U']
clip2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display_1.DataAxesGrid = 'GridAxesRepresentation'
clip2Display_1.PolarAxes = 'PolarAxesRepresentation'
clip2Display_1.ScalarOpacityFunction = alphawaterPWF
clip2Display_1.ScalarOpacityUnitDistance = 0.0024538375404105587
clip2Display_1.OpacityArrayName = ['POINTS', 'U']
clip2Display_1.SelectInputVectors = ['POINTS', 'U']
clip2Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display_1.ScaleTransferFunction.Points = [-0.016240447759628296, 0.0, 0.5, 0.0, 0.001265426748432219, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display_1.OpacityTransferFunction.Points = [-0.016240447759628296, 0.0, 0.5, 0.0, 0.001265426748432219, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractTimeSteps2, renderView1)

# show color bar/color legend
clip2Display_1.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(extractTimeSteps2)

# show data in view
extractTimeSteps2Display = Show(extractTimeSteps2, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
extractTimeSteps2Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip2, renderView1)

# set active source
SetActiveSource(clip2)

# show data in view
clip2Display_1 = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
clip2Display_1.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(extractTimeSteps2)

# hide data in view
Hide(clip2, renderView1)

# show data in view
extractTimeSteps2Display = Show(extractTimeSteps2, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
extractTimeSteps2Display.SetScalarBarVisibility(renderView1, True)

# destroy clip2
Delete(clip2)
del clip2

# set active source
SetActiveSource(extractTimeSteps1)

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=extractTimeSteps1)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['POINTS', 'alpha.water']
clip2.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [-0.014999999664723873, 0.0, 0.015]
clip2.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip2Display_1 = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip2Display_1.Representation = 'Surface'
clip2Display_1.ColorArrayName = ['CELLS', 'alpha.water']
clip2Display_1.LookupTable = alphawaterLUT
clip2Display_1.SelectTCoordArray = 'None'
clip2Display_1.SelectNormalArray = 'None'
clip2Display_1.SelectTangentArray = 'None'
clip2Display_1.OSPRayScaleArray = 'U'
clip2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display_1.SelectOrientationVectors = 'None'
clip2Display_1.ScaleFactor = 0.00599999986588955
clip2Display_1.SelectScaleArray = 'None'
clip2Display_1.GlyphType = 'Arrow'
clip2Display_1.GlyphTableIndexArray = 'None'
clip2Display_1.GaussianRadius = 0.00029999999329447744
clip2Display_1.SetScaleArray = ['POINTS', 'U']
clip2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display_1.OpacityArray = ['POINTS', 'U']
clip2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display_1.DataAxesGrid = 'GridAxesRepresentation'
clip2Display_1.PolarAxes = 'PolarAxesRepresentation'
clip2Display_1.ScalarOpacityFunction = alphawaterPWF
clip2Display_1.ScalarOpacityUnitDistance = 0.0024378942183546507
clip2Display_1.OpacityArrayName = ['POINTS', 'U']
clip2Display_1.SelectInputVectors = ['POINTS', 'U']
clip2Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display_1.ScaleTransferFunction.Points = [-0.1690545529127121, 0.0, 0.5, 0.0, 0.19370755553245544, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display_1.OpacityTransferFunction.Points = [-0.1690545529127121, 0.0, 0.5, 0.0, 0.19370755553245544, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractTimeSteps1, renderView1)

# show color bar/color legend
clip2Display_1.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=clip2.ClipType)

# set active source
SetActiveSource(clip1)

# create a new 'Extract Time Steps'
extractTimeSteps3 = ExtractTimeSteps(registrationName='ExtractTimeSteps3', Input=clip1)
extractTimeSteps3.TimeStepIndices = [0]
extractTimeSteps3.TimeStepRange = [0, 25]

# Properties modified on extractTimeSteps3
extractTimeSteps3.TimeStepIndices = [10]

# show data in view
extractTimeSteps3Display = Show(extractTimeSteps3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractTimeSteps3Display.Representation = 'Surface'
extractTimeSteps3Display.ColorArrayName = [None, '']
extractTimeSteps3Display.SelectTCoordArray = 'None'
extractTimeSteps3Display.SelectNormalArray = 'None'
extractTimeSteps3Display.SelectTangentArray = 'None'
extractTimeSteps3Display.OSPRayScaleArray = 'U'
extractTimeSteps3Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractTimeSteps3Display.SelectOrientationVectors = 'None'
extractTimeSteps3Display.ScaleFactor = 0.010000000149011612
extractTimeSteps3Display.SelectScaleArray = 'None'
extractTimeSteps3Display.GlyphType = 'Arrow'
extractTimeSteps3Display.GlyphTableIndexArray = 'None'
extractTimeSteps3Display.GaussianRadius = 0.0005000000074505806
extractTimeSteps3Display.SetScaleArray = ['POINTS', 'U']
extractTimeSteps3Display.ScaleTransferFunction = 'PiecewiseFunction'
extractTimeSteps3Display.OpacityArray = ['POINTS', 'U']
extractTimeSteps3Display.OpacityTransferFunction = 'PiecewiseFunction'
extractTimeSteps3Display.DataAxesGrid = 'GridAxesRepresentation'
extractTimeSteps3Display.PolarAxes = 'PolarAxesRepresentation'
extractTimeSteps3Display.ScalarOpacityUnitDistance = 0.0023104341326346937
extractTimeSteps3Display.OpacityArrayName = ['POINTS', 'U']
extractTimeSteps3Display.SelectInputVectors = ['POINTS', 'U']
extractTimeSteps3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractTimeSteps3Display.ScaleTransferFunction.Points = [-0.13635259866714478, 0.0, 0.5, 0.0, 0.12960238754749298, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractTimeSteps3Display.OpacityTransferFunction.Points = [-0.13635259866714478, 0.0, 0.5, 0.0, 0.12960238754749298, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(extractTimeSteps3Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
extractTimeSteps3Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(extractTimeSteps2)

# create a new 'Clip'
clip3 = Clip(registrationName='Clip3', Input=extractTimeSteps2)
clip3.ClipType = 'Plane'
clip3.HyperTreeGridClipper = 'Plane'
clip3.Scalars = ['POINTS', 'alpha.water']
clip3.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip3.ClipType.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip3.HyperTreeGridClipper.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=clip3.ClipType)

# set active source
SetActiveSource(extractTimeSteps3)

# set scalar coloring
ColorBy(extractTimeSteps3Display, ('CELLS', 'alpha.water'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
extractTimeSteps3Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
extractTimeSteps3Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(clip3)

# show data in view
clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip3Display.Representation = 'Surface'
clip3Display.ColorArrayName = ['CELLS', 'alpha.water']
clip3Display.LookupTable = alphawaterLUT
clip3Display.SelectTCoordArray = 'None'
clip3Display.SelectNormalArray = 'None'
clip3Display.SelectTangentArray = 'None'
clip3Display.OSPRayScaleArray = 'U'
clip3Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip3Display.SelectOrientationVectors = 'None'
clip3Display.ScaleFactor = 0.010000000149011612
clip3Display.SelectScaleArray = 'None'
clip3Display.GlyphType = 'Arrow'
clip3Display.GlyphTableIndexArray = 'None'
clip3Display.GaussianRadius = 0.0005000000074505806
clip3Display.SetScaleArray = ['POINTS', 'U']
clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
clip3Display.OpacityArray = ['POINTS', 'U']
clip3Display.OpacityTransferFunction = 'PiecewiseFunction'
clip3Display.DataAxesGrid = 'GridAxesRepresentation'
clip3Display.PolarAxes = 'PolarAxesRepresentation'
clip3Display.ScalarOpacityFunction = alphawaterPWF
clip3Display.ScalarOpacityUnitDistance = 0.003643411465705274
clip3Display.OpacityArrayName = ['POINTS', 'U']
clip3Display.SelectInputVectors = ['POINTS', 'U']
clip3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip3Display.ScaleTransferFunction.Points = [-0.0017067879671230912, 0.0, 0.5, 0.0, 0.0019288425100967288, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip3Display.OpacityTransferFunction.Points = [-0.0017067879671230912, 0.0, 0.5, 0.0, 0.0019288425100967288, 1.0, 0.5, 0.0]

# show color bar/color legend
clip3Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(extractTimeSteps3, renderView1)

# set active source
SetActiveSource(extractTimeSteps3)

# show data in view
extractTimeSteps3Display = Show(extractTimeSteps3, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
extractTimeSteps3Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on clip3.ClipType
clip3.ClipType.Origin = [-0.014999999664723873, 0.0, 0.025]
clip3.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

# hide data in view
Hide(extractTimeSteps2, renderView1)

# show color bar/color legend
clip3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(extractTimeSteps2)

# show data in view
extractTimeSteps2Display = Show(extractTimeSteps2, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
extractTimeSteps2Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(extractTimeSteps2, renderView1)

# hide data in view
Hide(extractTimeSteps3, renderView1)

# set active source
SetActiveSource(extractTimeSteps3)

# show data in view
extractTimeSteps3Display = Show(extractTimeSteps3, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
extractTimeSteps3Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip2, renderView1)

# set active source
SetActiveSource(clip2)

# show data in view
clip2Display_1 = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
clip2Display_1.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip3, renderView1)

# set active source
SetActiveSource(clip3)

# show data in view
clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
clip3Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(extractTimeSteps3, renderView1)

# hide data in view
Hide(clip3, renderView1)

# show data in view
clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
clip3Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(extractTimeSteps2)

# hide data in view
Hide(clip3, renderView1)

# show data in view
extractTimeSteps2Display = Show(extractTimeSteps2, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
extractTimeSteps2Display.SetScalarBarVisibility(renderView1, True)

# destroy clip3
Delete(clip3)
del clip3

# set active source
SetActiveSource(clip2)

# set active source
SetActiveSource(extractTimeSteps1)

# hide data in view
Hide(clip2, renderView1)

# show data in view
extractTimeSteps1Display = Show(extractTimeSteps1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
extractTimeSteps1Display.SetScalarBarVisibility(renderView1, True)

# destroy clip2
Delete(clip2)
del clip2

# set active source
SetActiveSource(extractTimeSteps2)

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=extractTimeSteps2)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['POINTS', 'alpha.water']
clip2.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [-0.014999999664723873, 0.0, 0.015]
clip2.ClipType.Normal = [0.0, 0.0, -1.0]

# show data in view
clip2Display_1 = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip2Display_1.Representation = 'Surface'
clip2Display_1.ColorArrayName = ['CELLS', 'alpha.water']
clip2Display_1.LookupTable = alphawaterLUT
clip2Display_1.SelectTCoordArray = 'None'
clip2Display_1.SelectNormalArray = 'None'
clip2Display_1.SelectTangentArray = 'None'
clip2Display_1.OSPRayScaleArray = 'U'
clip2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display_1.SelectOrientationVectors = 'None'
clip2Display_1.ScaleFactor = 0.008500000182539226
clip2Display_1.SelectScaleArray = 'None'
clip2Display_1.GlyphType = 'Arrow'
clip2Display_1.GlyphTableIndexArray = 'None'
clip2Display_1.GaussianRadius = 0.00042500000912696126
clip2Display_1.SetScaleArray = ['POINTS', 'U']
clip2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display_1.OpacityArray = ['POINTS', 'U']
clip2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display_1.DataAxesGrid = 'GridAxesRepresentation'
clip2Display_1.PolarAxes = 'PolarAxesRepresentation'
clip2Display_1.ScalarOpacityFunction = alphawaterPWF
clip2Display_1.ScalarOpacityUnitDistance = 0.002196195727358304
clip2Display_1.OpacityArrayName = ['POINTS', 'U']
clip2Display_1.SelectInputVectors = ['POINTS', 'U']
clip2Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display_1.ScaleTransferFunction.Points = [-0.15456044673919678, 0.0, 0.5, 0.0, 0.18777643144130707, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display_1.OpacityTransferFunction.Points = [-0.15456044673919678, 0.0, 0.5, 0.0, 0.18777643144130707, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractTimeSteps2, renderView1)

# show color bar/color legend
clip2Display_1.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(extractTimeSteps3)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=clip2.ClipType)

# create a new 'Clip'
clip3 = Clip(registrationName='Clip3', Input=extractTimeSteps3)
clip3.ClipType = 'Plane'
clip3.HyperTreeGridClipper = 'Plane'
clip3.Scalars = ['POINTS', 'alpha.water']
clip3.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip3.ClipType.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip3.HyperTreeGridClipper.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# Properties modified on clip3.ClipType
clip3.ClipType.Origin = [-0.014999999664723873, 0.0, 0.022]
clip3.ClipType.Normal = [0.0, 0.0, -1.0]

# show data in view
clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip3Display.Representation = 'Surface'
clip3Display.ColorArrayName = ['CELLS', 'alpha.water']
clip3Display.LookupTable = alphawaterLUT
clip3Display.SelectTCoordArray = 'None'
clip3Display.SelectNormalArray = 'None'
clip3Display.SelectTangentArray = 'None'
clip3Display.OSPRayScaleArray = 'U'
clip3Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip3Display.SelectOrientationVectors = 'None'
clip3Display.ScaleFactor = 0.007800000160932541
clip3Display.SelectScaleArray = 'None'
clip3Display.GlyphType = 'Arrow'
clip3Display.GlyphTableIndexArray = 'None'
clip3Display.GaussianRadius = 0.00039000000804662705
clip3Display.SetScaleArray = ['POINTS', 'U']
clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
clip3Display.OpacityArray = ['POINTS', 'U']
clip3Display.OpacityTransferFunction = 'PiecewiseFunction'
clip3Display.DataAxesGrid = 'GridAxesRepresentation'
clip3Display.PolarAxes = 'PolarAxesRepresentation'
clip3Display.ScalarOpacityFunction = alphawaterPWF
clip3Display.ScalarOpacityUnitDistance = 0.002146874909741927
clip3Display.OpacityArrayName = ['POINTS', 'U']
clip3Display.SelectInputVectors = ['POINTS', 'U']
clip3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip3Display.ScaleTransferFunction.Points = [-0.13635259866714478, 0.0, 0.5, 0.0, 0.12960238754749298, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip3Display.OpacityTransferFunction.Points = [-0.13635259866714478, 0.0, 0.5, 0.0, 0.12960238754749298, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractTimeSteps3, renderView1)

# show color bar/color legend
clip3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip1)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=clip3.ClipType)

# create a new 'Extract Time Steps'
extractTimeSteps4 = ExtractTimeSteps(registrationName='ExtractTimeSteps4', Input=clip1)
extractTimeSteps4.TimeStepIndices = [0]
extractTimeSteps4.TimeStepRange = [0, 25]

# Properties modified on extractTimeSteps4
extractTimeSteps4.TimeStepIndices = [15]

# show data in view
extractTimeSteps4Display = Show(extractTimeSteps4, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractTimeSteps4Display.Representation = 'Surface'
extractTimeSteps4Display.ColorArrayName = [None, '']
extractTimeSteps4Display.SelectTCoordArray = 'None'
extractTimeSteps4Display.SelectNormalArray = 'None'
extractTimeSteps4Display.SelectTangentArray = 'None'
extractTimeSteps4Display.OSPRayScaleArray = 'U'
extractTimeSteps4Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractTimeSteps4Display.SelectOrientationVectors = 'None'
extractTimeSteps4Display.ScaleFactor = 0.010000000149011612
extractTimeSteps4Display.SelectScaleArray = 'None'
extractTimeSteps4Display.GlyphType = 'Arrow'
extractTimeSteps4Display.GlyphTableIndexArray = 'None'
extractTimeSteps4Display.GaussianRadius = 0.0005000000074505806
extractTimeSteps4Display.SetScaleArray = ['POINTS', 'U']
extractTimeSteps4Display.ScaleTransferFunction = 'PiecewiseFunction'
extractTimeSteps4Display.OpacityArray = ['POINTS', 'U']
extractTimeSteps4Display.OpacityTransferFunction = 'PiecewiseFunction'
extractTimeSteps4Display.DataAxesGrid = 'GridAxesRepresentation'
extractTimeSteps4Display.PolarAxes = 'PolarAxesRepresentation'
extractTimeSteps4Display.ScalarOpacityUnitDistance = 0.0023104341326346937
extractTimeSteps4Display.OpacityArrayName = ['POINTS', 'U']
extractTimeSteps4Display.SelectInputVectors = ['POINTS', 'U']
extractTimeSteps4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractTimeSteps4Display.ScaleTransferFunction.Points = [-0.10882004350423813, 0.0, 0.5, 0.0, 0.1058594137430191, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractTimeSteps4Display.OpacityTransferFunction.Points = [-0.10882004350423813, 0.0, 0.5, 0.0, 0.1058594137430191, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(extractTimeSteps4Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
extractTimeSteps4Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Clip'
clip4 = Clip(registrationName='Clip4', Input=extractTimeSteps4)
clip4.ClipType = 'Plane'
clip4.HyperTreeGridClipper = 'Plane'
clip4.Scalars = ['POINTS', 'alpha.water']
clip4.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip4.ClipType.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip4.HyperTreeGridClipper.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# set active source
SetActiveSource(extractTimeSteps4)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=clip4.ClipType)

# set scalar coloring
ColorBy(extractTimeSteps4Display, ('CELLS', 'alpha.water'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
extractTimeSteps4Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
extractTimeSteps4Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(clip4)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=clip4.ClipType)

# Properties modified on clip4.ClipType
clip4.ClipType.Origin = [-0.014999999664723873, 0.0, 0.028]
clip4.ClipType.Normal = [0.0, 0.0, -1.0]

# show data in view
clip4Display = Show(clip4, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip4Display.Representation = 'Surface'
clip4Display.ColorArrayName = ['CELLS', 'alpha.water']
clip4Display.LookupTable = alphawaterLUT
clip4Display.SelectTCoordArray = 'None'
clip4Display.SelectNormalArray = 'None'
clip4Display.SelectTangentArray = 'None'
clip4Display.OSPRayScaleArray = 'U'
clip4Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip4Display.SelectOrientationVectors = 'None'
clip4Display.ScaleFactor = 0.007200000062584877
clip4Display.SelectScaleArray = 'None'
clip4Display.GlyphType = 'Arrow'
clip4Display.GlyphTableIndexArray = 'None'
clip4Display.GaussianRadius = 0.00036000000312924385
clip4Display.SetScaleArray = ['POINTS', 'U']
clip4Display.ScaleTransferFunction = 'PiecewiseFunction'
clip4Display.OpacityArray = ['POINTS', 'U']
clip4Display.OpacityTransferFunction = 'PiecewiseFunction'
clip4Display.DataAxesGrid = 'GridAxesRepresentation'
clip4Display.PolarAxes = 'PolarAxesRepresentation'
clip4Display.ScalarOpacityFunction = alphawaterPWF
clip4Display.ScalarOpacityUnitDistance = 0.0021039063117933234
clip4Display.OpacityArrayName = ['POINTS', 'U']
clip4Display.SelectInputVectors = ['POINTS', 'U']
clip4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip4Display.ScaleTransferFunction.Points = [-0.10882004350423813, 0.0, 0.5, 0.0, 0.1058594137430191, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip4Display.OpacityTransferFunction.Points = [-0.10882004350423813, 0.0, 0.5, 0.0, 0.1058594137430191, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractTimeSteps4, renderView1)

# show color bar/color legend
clip4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on clip4.ClipType
clip4.ClipType.Origin = [-0.014999999664723873, 0.0, 0.035]

# update the view to ensure updated data information
renderView1.Update()

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=clip4.ClipType)

# set active source
SetActiveSource(clip1)

# create a new 'Extract Time Steps'
extractTimeSteps5 = ExtractTimeSteps(registrationName='ExtractTimeSteps5', Input=clip1)
extractTimeSteps5.TimeStepIndices = [0]
extractTimeSteps5.TimeStepRange = [0, 25]

# Properties modified on extractTimeSteps5
extractTimeSteps5.TimeStepIndices = [20]

# show data in view
extractTimeSteps5Display = Show(extractTimeSteps5, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractTimeSteps5Display.Representation = 'Surface'
extractTimeSteps5Display.ColorArrayName = [None, '']
extractTimeSteps5Display.SelectTCoordArray = 'None'
extractTimeSteps5Display.SelectNormalArray = 'None'
extractTimeSteps5Display.SelectTangentArray = 'None'
extractTimeSteps5Display.OSPRayScaleArray = 'U'
extractTimeSteps5Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractTimeSteps5Display.SelectOrientationVectors = 'None'
extractTimeSteps5Display.ScaleFactor = 0.010000000149011612
extractTimeSteps5Display.SelectScaleArray = 'None'
extractTimeSteps5Display.GlyphType = 'Arrow'
extractTimeSteps5Display.GlyphTableIndexArray = 'None'
extractTimeSteps5Display.GaussianRadius = 0.0005000000074505806
extractTimeSteps5Display.SetScaleArray = ['POINTS', 'U']
extractTimeSteps5Display.ScaleTransferFunction = 'PiecewiseFunction'
extractTimeSteps5Display.OpacityArray = ['POINTS', 'U']
extractTimeSteps5Display.OpacityTransferFunction = 'PiecewiseFunction'
extractTimeSteps5Display.DataAxesGrid = 'GridAxesRepresentation'
extractTimeSteps5Display.PolarAxes = 'PolarAxesRepresentation'
extractTimeSteps5Display.ScalarOpacityUnitDistance = 0.0023104341326346937
extractTimeSteps5Display.OpacityArrayName = ['POINTS', 'U']
extractTimeSteps5Display.SelectInputVectors = ['POINTS', 'U']
extractTimeSteps5Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractTimeSteps5Display.ScaleTransferFunction.Points = [-0.10116937011480331, 0.0, 0.5, 0.0, 0.07538716495037079, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractTimeSteps5Display.OpacityTransferFunction.Points = [-0.10116937011480331, 0.0, 0.5, 0.0, 0.07538716495037079, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(extractTimeSteps5Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
extractTimeSteps5Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(extractTimeSteps5Display, ('CELLS', 'alpha.water'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
extractTimeSteps5Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
extractTimeSteps5Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Clip'
clip5 = Clip(registrationName='Clip5', Input=extractTimeSteps5)
clip5.ClipType = 'Plane'
clip5.HyperTreeGridClipper = 'Plane'
clip5.Scalars = ['POINTS', 'alpha.water']
clip5.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip5.ClipType.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip5.HyperTreeGridClipper.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# Properties modified on clip5.ClipType
clip5.ClipType.Origin = [-0.014999999664723873, 0.0, 0.045]
clip5.ClipType.Normal = [0.0, 0.0, -1.0]

# show data in view
clip5Display = Show(clip5, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip5Display.Representation = 'Surface'
clip5Display.ColorArrayName = ['CELLS', 'alpha.water']
clip5Display.LookupTable = alphawaterLUT
clip5Display.SelectTCoordArray = 'None'
clip5Display.SelectNormalArray = 'None'
clip5Display.SelectTangentArray = 'None'
clip5Display.OSPRayScaleArray = 'U'
clip5Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip5Display.SelectOrientationVectors = 'None'
clip5Display.ScaleFactor = 0.00599999986588955
clip5Display.SelectScaleArray = 'None'
clip5Display.GlyphType = 'Arrow'
clip5Display.GlyphTableIndexArray = 'None'
clip5Display.GaussianRadius = 0.00029999999329447744
clip5Display.SetScaleArray = ['POINTS', 'U']
clip5Display.ScaleTransferFunction = 'PiecewiseFunction'
clip5Display.OpacityArray = ['POINTS', 'U']
clip5Display.OpacityTransferFunction = 'PiecewiseFunction'
clip5Display.DataAxesGrid = 'GridAxesRepresentation'
clip5Display.PolarAxes = 'PolarAxesRepresentation'
clip5Display.ScalarOpacityFunction = alphawaterPWF
clip5Display.ScalarOpacityUnitDistance = 0.002025990493526319
clip5Display.OpacityArrayName = ['POINTS', 'U']
clip5Display.SelectInputVectors = ['POINTS', 'U']
clip5Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip5Display.ScaleTransferFunction.Points = [-0.10116937011480331, 0.0, 0.5, 0.0, 0.07538716495037079, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip5Display.OpacityTransferFunction.Points = [-0.10116937011480331, 0.0, 0.5, 0.0, 0.07538716495037079, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractTimeSteps5, renderView1)

# show color bar/color legend
clip5Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=clip5.ClipType)

# set active source
SetActiveSource(clip1)

# create a new 'Extract Time Steps'
extractTimeSteps6 = ExtractTimeSteps(registrationName='ExtractTimeSteps6', Input=clip1)
extractTimeSteps6.TimeStepIndices = [0]
extractTimeSteps6.TimeStepRange = [0, 25]

# Properties modified on extractTimeSteps6
extractTimeSteps6.TimeStepIndices = [25]

# show data in view
extractTimeSteps6Display = Show(extractTimeSteps6, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
extractTimeSteps6Display.Representation = 'Surface'
extractTimeSteps6Display.ColorArrayName = [None, '']
extractTimeSteps6Display.SelectTCoordArray = 'None'
extractTimeSteps6Display.SelectNormalArray = 'None'
extractTimeSteps6Display.SelectTangentArray = 'None'
extractTimeSteps6Display.OSPRayScaleArray = 'U'
extractTimeSteps6Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractTimeSteps6Display.SelectOrientationVectors = 'None'
extractTimeSteps6Display.ScaleFactor = 0.010000000149011612
extractTimeSteps6Display.SelectScaleArray = 'None'
extractTimeSteps6Display.GlyphType = 'Arrow'
extractTimeSteps6Display.GlyphTableIndexArray = 'None'
extractTimeSteps6Display.GaussianRadius = 0.0005000000074505806
extractTimeSteps6Display.SetScaleArray = ['POINTS', 'U']
extractTimeSteps6Display.ScaleTransferFunction = 'PiecewiseFunction'
extractTimeSteps6Display.OpacityArray = ['POINTS', 'U']
extractTimeSteps6Display.OpacityTransferFunction = 'PiecewiseFunction'
extractTimeSteps6Display.DataAxesGrid = 'GridAxesRepresentation'
extractTimeSteps6Display.PolarAxes = 'PolarAxesRepresentation'
extractTimeSteps6Display.ScalarOpacityUnitDistance = 0.0023104341326346937
extractTimeSteps6Display.OpacityArrayName = ['POINTS', 'U']
extractTimeSteps6Display.SelectInputVectors = ['POINTS', 'U']
extractTimeSteps6Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractTimeSteps6Display.ScaleTransferFunction.Points = [-0.2514200508594513, 0.0, 0.5, 0.0, 0.3535236716270447, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractTimeSteps6Display.OpacityTransferFunction.Points = [-0.2514200508594513, 0.0, 0.5, 0.0, 0.3535236716270447, 1.0, 0.5, 0.0]

# hide data in view
Hide(clip1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(extractTimeSteps6Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
extractTimeSteps6Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(extractTimeSteps6Display, ('CELLS', 'alpha.water'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
extractTimeSteps6Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
extractTimeSteps6Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Clip'
clip6 = Clip(registrationName='Clip6', Input=extractTimeSteps6)
clip6.ClipType = 'Plane'
clip6.HyperTreeGridClipper = 'Plane'
clip6.Scalars = ['POINTS', 'alpha.water']
clip6.Value = 0.5000019669532776

# init the 'Plane' selected for 'ClipType'
clip6.ClipType.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip6.HyperTreeGridClipper.Origin = [-0.014999999664723873, 0.0, 0.05000000074505806]

# Properties modified on clip6.ClipType
clip6.ClipType.Origin = [-0.014999999664723873, 0.0, 0.055]
clip6.ClipType.Normal = [0.0, 0.0, -1.0]

# show data in view
clip6Display = Show(clip6, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip6Display.Representation = 'Surface'
clip6Display.ColorArrayName = ['CELLS', 'alpha.water']
clip6Display.LookupTable = alphawaterLUT
clip6Display.SelectTCoordArray = 'None'
clip6Display.SelectNormalArray = 'None'
clip6Display.SelectTangentArray = 'None'
clip6Display.OSPRayScaleArray = 'U'
clip6Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip6Display.SelectOrientationVectors = 'None'
clip6Display.ScaleFactor = 0.00599999986588955
clip6Display.SelectScaleArray = 'None'
clip6Display.GlyphType = 'Arrow'
clip6Display.GlyphTableIndexArray = 'None'
clip6Display.GaussianRadius = 0.00029999999329447744
clip6Display.SetScaleArray = ['POINTS', 'U']
clip6Display.ScaleTransferFunction = 'PiecewiseFunction'
clip6Display.OpacityArray = ['POINTS', 'U']
clip6Display.OpacityTransferFunction = 'PiecewiseFunction'
clip6Display.DataAxesGrid = 'GridAxesRepresentation'
clip6Display.PolarAxes = 'PolarAxesRepresentation'
clip6Display.ScalarOpacityFunction = alphawaterPWF
clip6Display.ScalarOpacityUnitDistance = 0.002021808885705089
clip6Display.OpacityArrayName = ['POINTS', 'U']
clip6Display.SelectInputVectors = ['POINTS', 'U']
clip6Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip6Display.ScaleTransferFunction.Points = [-0.2514200508594513, 0.0, 0.5, 0.0, 0.3535236716270447, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip6Display.OpacityTransferFunction.Points = [-0.2514200508594513, 0.0, 0.5, 0.0, 0.3535236716270447, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractTimeSteps6, renderView1)

# show color bar/color legend
clip6Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=clip6.ClipType)

# set active source
SetActiveSource(a6mmTurOpenFOAM)

# get display properties
a6mmTurOpenFOAMDisplay = GetDisplayProperties(a6mmTurOpenFOAM, view=renderView1)

# create a new 'Clip'
clip7 = Clip(registrationName='Clip7', Input=a6mmTurOpenFOAM)
clip7.ClipType = 'Plane'
clip7.HyperTreeGridClipper = 'Plane'
clip7.Scalars = ['POINTS', 'alpha.water']
clip7.Value = 0.5

# init the 'Plane' selected for 'ClipType'
clip7.ClipType.Origin = [0.0, 0.0, 0.05000000074505806]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip7.HyperTreeGridClipper.Origin = [0.0, 0.0, 0.05000000074505806]

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=clip7.ClipType)

# show data in view
clip7Display = Show(clip7, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip7Display.Representation = 'Surface'
clip7Display.ColorArrayName = [None, '']
clip7Display.SelectTCoordArray = 'None'
clip7Display.SelectNormalArray = 'None'
clip7Display.SelectTangentArray = 'None'
clip7Display.OSPRayScaleArray = 'U'
clip7Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip7Display.SelectOrientationVectors = 'None'
clip7Display.ScaleFactor = 0.010000000149011612
clip7Display.SelectScaleArray = 'None'
clip7Display.GlyphType = 'Arrow'
clip7Display.GlyphTableIndexArray = 'None'
clip7Display.GaussianRadius = 0.0005000000074505806
clip7Display.SetScaleArray = ['POINTS', 'U']
clip7Display.ScaleTransferFunction = 'PiecewiseFunction'
clip7Display.OpacityArray = ['POINTS', 'U']
clip7Display.OpacityTransferFunction = 'PiecewiseFunction'
clip7Display.DataAxesGrid = 'GridAxesRepresentation'
clip7Display.PolarAxes = 'PolarAxesRepresentation'
clip7Display.ScalarOpacityUnitDistance = 0.0023104341326346937
clip7Display.OpacityArrayName = ['POINTS', 'U']
clip7Display.SelectInputVectors = ['POINTS', 'U']
clip7Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip7Display.ScaleTransferFunction.Points = [-0.1690545529127121, 0.0, 0.5, 0.0, 0.19370755553245544, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip7Display.OpacityTransferFunction.Points = [-0.1690545529127121, 0.0, 0.5, 0.0, 0.19370755553245544, 1.0, 0.5, 0.0]

# hide data in view
Hide(a6mmTurOpenFOAM, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(clip7Display, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
clip7Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip7, renderView1)

# change representation type
clip7Display.SetRepresentationType('Wireframe')

# set active source
SetActiveSource(clip7)

# show data in view
clip7Display = Show(clip7, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
clip7Display.SetScalarBarVisibility(renderView1, True)

# turn off scalar coloring
ColorBy(clip7Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# change solid color
clip7Display.AmbientColor = [0.7411764705882353, 0.7411764705882353, 0.7411764705882353]
clip7Display.DiffuseColor = [0.7411764705882353, 0.7411764705882353, 0.7411764705882353]

# Properties modified on clip7Display
clip7Display.Opacity = 0.25

# Properties modified on clip7Display
clip7Display.RenderLinesAsTubes = 1

renderView1.ResetActiveCameraToNegativeX()

# reset view to fit data
renderView1.ResetCamera(False)

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1028, 773)

# current camera placement for renderView1
renderView1.CameraPosition = [0.21762574497938478, 0.0, 0.05000000074505806]
renderView1.CameraFocalPoint = [-0.014999999664723873, 0.0, 0.05000000074505806]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.06020797309505103

# save screenshot
SaveScreenshot('/home/viseol/OpenFOAM/viseol-13/run/rising_Incompressible/6mmTur/6mmTur.png', renderView1, ImageResolution=[1028, 773])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1028, 773)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.21762574497938478, 0.0, 0.05000000074505806]
renderView1.CameraFocalPoint = [-0.014999999664723873, 0.0, 0.05000000074505806]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.06020797309505103

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).