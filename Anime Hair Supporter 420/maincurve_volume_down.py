import bpy

class ahs_maincurve_volume_down(bpy.types.Operator):
	bl_idname = 'object.ahs_maincurve_volume_down'
	bl_label = "肉付けを削除"
	bl_description = "選択カーブの設定したテーパー/ベベルを削除"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		try:
			for ob in context.selected_objects:
				if ob.type != 'CURVE': continue
				if ob.data.taper_object or ob.data.bevel_object: break
			else: return False
		except: return False
		return True
	
	def execute(self, context):
		for ob in context.selected_objects:
			if ob.type != 'CURVE': continue
			if ob.data.taper_object:
				context.blend_data.curves.remove(ob.data.taper_object.data, do_unlink=True)
			if ob.data.bevel_object:
				context.blend_data.curves.remove(ob.data.bevel_object.data, do_unlink=True)
		
		for area in context.screen.areas: area.tag_redraw()
		return {'FINISHED'}
