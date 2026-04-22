func twoEditWords(queries, dictionary []string) []string {
	result := []string{}
	for _, q := range queries {
		for _, d := range dictionary {
			diff := 0
			for i := 0; i < len(q); i++ {
				if q[i] != d[i] {
					diff++
				}
				if diff > 2 {
					break
				}
			}
			if diff <= 2 {
				result = append(result, q)
				break
			}
		}
	}
	return result
}