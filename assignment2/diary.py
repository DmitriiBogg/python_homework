import traceback

try:
    with open("diary.txt", "a") as file:
        first_prompt = True
        while True:
            prompt = "What happened today? " if first_prompt else "What else? "
            first_prompt = False
            line = input(prompt)

            file.write(line + "\n")

            if line.strip().lower() == "done for now":
                break

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = [
        f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
        for trace in trace_back
    ]

    print("An exception occurred.")
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
