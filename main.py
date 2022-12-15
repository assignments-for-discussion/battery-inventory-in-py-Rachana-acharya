
def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  if (count["lowCount"]<count_batteries_by_usage[1]):
    assert(counts["lowCount"] == 2)
    return lowCount
  elif (count["highCount"]>count_batteries_by_usage[4]):
    assert(counts["highCount"] == 1)
    return highCount   
  else:
    assert(counts["mediumCount"] == 3)
    return mediumCount
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
