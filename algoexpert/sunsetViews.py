def sunsetViews(buildings, direction):
	sunset_builds = []
	current = 0
    if direction == "EAST":
		for i in reversed(range(len(buildings))):
			if buildings[i] > current:
				current = buildings[i]
				sunset_builds.append(i)
	else:
		for i in range(len(buildings)):
			if buildings[i] > current:
				current = buildings[i]
				sunset_builds.append(i)
	return sorted(sunset_builds)
		
