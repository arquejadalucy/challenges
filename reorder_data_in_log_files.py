class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digit_logs = []
        letter_logs = []

        for log in logs:
            if log[-1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        # "let1 art can bar"
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letter_logs + digit_logs
