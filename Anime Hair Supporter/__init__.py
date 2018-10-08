# アドオンを読み込む時に最初にこのファイルが読み込まれます

# アドオン情報
bl_info = {
	'name' : "Anime Hair Supporter",
	'author' : "saidenka",
	'version' : (1, 0),
	'blender' : (2, 79, 0),
	'location' : "3Dビュー > オブジェクトモード > ツールシェルフ > ツール > アニメ髪支援パネル",
	'description' : "",
	'warning' : "",
	'wiki_url' : "https://github.com/saidenka/Blender-AnimeHairSupporter",
	'tracker_url' : "https://github.com/saidenka/Blender-AnimeHairSupporter",
	'category' : "Tools"
}

# サブスクリプト群をインポート
if 'bpy' in locals():
	import imp
	imp.reload(_panel)
	
	imp.reload(convert_edgemesh_to_curve)
	imp.reload(convert_curve_to_edgemesh)
	
	imp.reload(maincurve_activate)
	imp.reload(maincurve_volume_up)
	imp.reload(maincurve_volume_down)
	imp.reload(maincurve_extra_deform)
	imp.reload(maincurve_gradation_tilt)
	imp.reload(maincurve_select)
	imp.reload(maincurve_hide)
	imp.reload(maincurve_set_resolution)
	imp.reload(maincurve_set_order)
	
	imp.reload(tapercurve_activate)
	imp.reload(tapercurve_id_singlize)
	imp.reload(tapercurve_change_type)
	imp.reload(tapercurve_mirror)
	imp.reload(tapercurve_relocation)
	imp.reload(tapercurve_remove_alones)
	imp.reload(tapercurve_select)
	imp.reload(tapercurve_hide)
	
	imp.reload(convert_curve_to_armature)
	imp.reload(convert_curve_to_mesh)
else:
	from . import _panel
	
	from . import convert_edgemesh_to_curve
	from . import convert_curve_to_edgemesh
	
	from . import maincurve_activate
	from . import maincurve_volume_up
	from . import maincurve_volume_down
	from . import maincurve_extra_deform
	from . import maincurve_gradation_tilt
	from . import maincurve_select
	from . import maincurve_hide
	from . import maincurve_set_resolution
	from . import maincurve_set_order
	
	from . import tapercurve_activate
	from . import tapercurve_id_singlize
	from . import tapercurve_change_type
	from . import tapercurve_mirror
	from . import tapercurve_relocation
	from . import tapercurve_remove_alones
	from . import tapercurve_select
	from . import tapercurve_hide
	
	from . import convert_curve_to_armature
	from . import convert_curve_to_mesh

# この位置に記述 (重要)
import bpy

class AHS_Props(bpy.types.PropertyGroup):
	maincurve_expand = bpy.props.BoolProperty(name="メインパネルを展開", default=True)
	tapercurve_expand = bpy.props.BoolProperty(name="テーパーパネルを展開", default=True)
	bevelcurve_expand = bpy.props.BoolProperty(name="ベベルパネルを展開", default=True)

classes = (
	convert_curve_to_armature.ahs_convert_curve_to_armature,
	convert_curve_to_edgemesh.ahs_convert_curve_to_edgemesh,
	convert_curve_to_mesh.ahs_convert_curve_to_mesh,
	convert_edgemesh_to_curve.ahs_convert_edgemesh_to_curve,
	maincurve_activate.ahs_maincurve_activate,
	maincurve_extra_deform.ahs_maincurve_extra_deform,
	maincurve_gradation_tilt.ahs_maincurve_gradation_tilt,
	maincurve_hide.ahs_maincurve_hide,
	maincurve_select.ahs_maincurve_select,
	maincurve_set_order.ahs_maincurve_set_order,
	maincurve_set_resolution.ahs_maincurve_set_resolution,
	maincurve_volume_down.ahs_maincurve_volume_down,
	maincurve_volume_up.ahs_maincurve_volume_up,
	tapercurve_activate.ahs_tapercurve_activate,
	tapercurve_change_type.ahs_tapercurve_change_type,
	tapercurve_hide.ahs_tapercurve_hide,
	tapercurve_id_singlize.ahs_tapercurve_id_singlize,
	tapercurve_mirror.ahs_tapercurve_mirror,
	tapercurve_relocation.ahs_tapercurve_relocation,
	tapercurve_remove_alones.ahs_tapercurve_remove_alones,
	tapercurve_select.ahs_tapercurve_select,
	_panel.VIEW3D_PT_tools_anime_hair_supporter,
	AHS_Props
)

# プラグインをインストールしたときの処理
def register():
		
	for cls in classes:
		bpy.utils.register_class(cls)

	bpy.types.Scene.ahs_props = bpy.props.PointerProperty(type=AHS_Props)

# プラグインをアンインストールしたときの処理
def unregister():
	if bpy.context.scene.get('ahs_props'): del bpy.context.scene['ahs_props']
	
	for cls in classes:
		bpy.utils.unregister_class(cls)

# 最初に実行される
if __name__ == '__main__':
	register()
