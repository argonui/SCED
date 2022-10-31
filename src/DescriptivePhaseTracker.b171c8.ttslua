function onLoad()
  -- Add a button to the object
  local params = {}
  params.click_function = 'toPhaseTwo'
  params.function_owner = self
  params.tooltip = '1. Mythos Phase\n\n    1.1 Round begins. Mythos phase begins.\n\n    1.2 Place 1 doom on the current agenda.\n\n    1.3 Check doom threshold.\n\n    1.4 Each investigator draws 1\n      encounter card.\n\n> PLAYER WINDOW <\n\n    1.5 Mythos phase ends.'
  params.width = 600
  params.height = 600
  self.createButton(params)
end

function toPhaseTwo()
  self.setState(2)
end