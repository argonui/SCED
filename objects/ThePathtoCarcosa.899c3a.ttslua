
function onload(saved_data)
    createDownloadButton()
end


--Beginning Setup


--Make Download button
function createDownloadButton()
    self.createButton({
        label="Download", click_function="buttonClick_download", function_owner=self,
        position={0,0.1,7}, rotation={0,0,0}, height=850, width=3300,
        font_size=700, color={0,0,0}, font_color={1,1,1}
    })
end

--Triggered by download button,
function buttonClick_download()
    local params = { url = self.getGMNotes(), replace = self.guid }
    Global.call('placeholder_download', params)
end