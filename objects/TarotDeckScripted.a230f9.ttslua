CARD_OFFSET = Vector({0, 0.1, -2})
ORIENTATIONS = { {0, 270, 0}, { 0, 90, 0} }
READING = {
    "Temperance",
    "Justice",
    "Hermit",
    "Hanged Man",
    "Hierophant",
    "Lovers",
    "Chariot",
    "Wheel of Fortune"
}

function onLoad()
    self.addContextMenuItem("Chaos", chaos, false)
    self.addContextMenuItem("Balance", balance, false)
    self.addContextMenuItem("Choice", choice, false)
    self.addContextMenuItem("Destiny (Campaign)", destiny, false)
    self.addContextMenuItem("Accept Your Fate", fate, false)

    math.randomseed(os.time())
end

function chaos(color)
    self.shuffle()
    self.takeObject({
        position = self.getPosition() + CARD_OFFSET,
        rotation = ORIENTATIONS[math.random(2)],
        smooth = true
    })
end

function balance(color)
    self.shuffle()
    self.takeObject({
        position = self.getPosition() + CARD_OFFSET,
        rotation = ORIENTATIONS[1],
        smooth = true
    })
    self.takeObject({
        position = self.getPosition() + 2*CARD_OFFSET,
        rotation = ORIENTATIONS[2],
        smooth = true
    })
end

function choice(color)
    self.shuffle()
    for i=1,3 do
        self.takeObject({
            position = self.getPosition() + i*CARD_OFFSET,
            rotation = ORIENTATIONS[1],
            smooth = true
        })
    end
    broadcastToColor("Choose and reverse two of the cards.", color)
end

function destiny(color)
    self.shuffle()
    for i=1,8 do
        self.takeObject({
            position = self.getPosition() + i*CARD_OFFSET,
            rotation = ORIENTATIONS[1],
            smooth = true
        })
    end
    broadcastToColor("Each card corresponds to one scenario, leftmost is first. Choose and reverse half of the cards (rounded up).", color)
end

function fate(color)
    local guids = {}
    local cards = self.getObjects()
    for i,card in ipairs(cards) do
        for j,reading in ipairs(READING) do
            if string.match(card.name, reading) ~= nil then
                guids[j] = card.guid
            end
        end
    end
    for k,guid in ipairs(guids) do
        self.takeObject({
            guid = guid,
            position = self.getPosition() + k*CARD_OFFSET,
            rotation = ORIENTATIONS[1],
            smooth = true
        })
    end
    broadcastToColor("Each card corresponds to one scenario, leftmost is first. Choose and reverse half of the cards (rounded up).", color)
end