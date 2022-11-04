function onLoad()
    local params = {}
    params.click_function = 'updateSurface'
    params.function_owner = self
    params.label = 'Apply'
    params.tooltip= 'Left click to apply image, right click to revert to default.'
    params.position = {0,0.05,-1.6}
    params.rotation = {0,0,0}
    params.height = 250
    params.width = 580
    params.color = {0,0,0}
    params.font_color = {1,1,1}
    self.createButton(params)
end

  function updateSurface(obj, color, alt_click)
     obj_surface = getObjectFromGUID("721ba2")
     local customInfo = obj_surface.getCustomObject()
     if alt_click == false then
        customInfo.image = "https://i.ibb.co/b2d8qvg/Dark-Matter-5-Strange-Moons-Hongyu-Yin.jpg"
     else
        customInfo.image = "http://cloud-3.steamusercontent.com/ugc/1717534454684871624/1739012BC3EA35E381D1172705B670BEEBD1AF6F/"
     end
     obj_surface.setCustomObject(customInfo)
     obj_surface = obj_surface.reload()
     broadcastToAll("New Playmat Image Applied", {0.2,0.9,0.2})
  end
