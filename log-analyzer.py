from pathlib import Path


def parse_logs(log_fh):
    log_list = []
    for line in log_fh:
        # Filter lines starting with '['
        if line.startswith("["):
            errorMessage = []
            # Consider only error log message
            if line.split(" ")[3] == "ERROR":
                log = line.split(" ")[0] + " " + line.split(" ")[1] + " " + \
                      line.split(" ")[2] + " " + line.split(" ")[3]

                # capture error message
                for i in range(5, len(line.split(" "))):
                    errorMessage.append(line.split(" ")[i])
                    err_log = " ".join(errorMessage)
                parsed_log = log + " - " + err_log
                log_list.append(parsed_log)

    return log_list


log_dir = "/Users/greenbook/Desktop/springboard/airflow-mini-project/airflowlogs/marketvol"

# get all the logs recursively under the log folder
file_list = Path(log_dir).rglob('*.log')

for file in file_list:
    with open(file) as f:
        print(f.name)
        dict1 = parse_logs(f)
    #    print("Error metrics for task '" + str(file).split("\\")[3] + "' on date: " + str(file).split("\\")[4])
        print("The total number of errors :" + str(len(dict1)))

        if len(dict1) > 0:
            print("Here are all the errors: ")
            for i in range(len(dict1)):
                print(dict1[i])
        print("----------------------------------------------------------------------------------------")
