import pandas as pd
from csv import writer
import datetime
from test_platform import TestPlatformEndpoints


file = pd.read_csv("D:\\Fountech AI\\Soffos\\platform test\\Test Result.csv")
df = pd.DataFrame(file)
# get current date
current_date = datetime.date.today()
print(df)
with open("D:\\Fountech AI\\Soffos\\platform test\\Test Result.csv", "a") as f_object:
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)
    List = ["a", "b", "c"]
    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(List)

    # Close the file object
    f_object.close()
a = TestPlatformEndpoints()
a.test_ambiguity_detection()


def ambiguity_test(date):
    source = "D:\\Fountech AI\\Soffos\\platform test\\Source\\ambiguity.txt"
    a = TestPlatformEndpoints()
    result = a.test_ambiguity_detection()
