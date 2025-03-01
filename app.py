from flask import Flask, render_template, request, jsonify
import subprocess
import os
import time
from datetime import datetime
import json

app = Flask(__name__)

# Sample coding challenges with skeleton code, wrapper templates, and test cases
CHALLENGES = {
    1: {
        "title": "Two Sum",
        "description": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.",
        "test_cases": [
            {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1], "case_name": "Case 1"},
            {"nums": [3, 2, 4], "target": 6, "expected": [1, 2], "case_name": "Case 2"},
            {"nums": [3, 3], "target": 6, "expected": [0, 1], "case_name": "Case 3"}
        ],
        "sample_input": "nums = [2, 7, 11, 15], target = 9",
        "sample_output": "[0, 1]",
        "skeleton_code": {
            "python": """
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Write your code here
""",
            "javascript": """
class Solution {
    twoSum(nums, target) {
        // Write your code here
    }
}
""",
            "java": """
public class Main {
    public int[] twoSum(int[] nums, int target) {
        // Write your code here
    }
}
"""
        },
        "wrapper_templates": {
            "python": """
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        {user_code}

# Wrapper code to handle I/O
if __name__ == "__main__":
    import json
    nums = json.loads(input())
    target = int(input())
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(json.dumps(result))
""",
            "javascript": """
class Solution {
    twoSum(nums, target) {
        {user_code}
    }
}

process.stdin.on('data', data => {
    const inputs = data.toString().trim().split('\\n');
    const nums = JSON.parse(inputs[0]);
    const target = parseInt(inputs[1]);
    const solution = new Solution();
    const result = solution.twoSum(nums, target);
    console.log(JSON.stringify(result));
    process.exit();
});
""",
            "java": """
import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public int[] twoSum(int[] nums, int target) {
        {user_code}
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String numsLine = sc.nextLine();
        int target = Integer.parseInt(sc.nextLine());
        int[] nums = Arrays.stream(numsLine.replaceAll("[\\[\\]]", "").split(","))
                           .mapToInt(Integer::parseInt)
                           .toArray();
        Main solution = new Main();
        int[] result = solution.twoSum(nums, target);
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < result.length; i++) {
            sb.append(result[i]);
            if (i < result.length - 1) sb.append(",");
        }
        sb.append("]");
        System.out.println(sb.toString());
        sc.close();
    }
}
"""
        }
    },
    2: {
        "title": "Reverse Integer",
        "description": "Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.",
        "test_cases": [
            {"x": 123, "expected": 321, "case_name": "Case 1"},
            {"x": -123, "expected": -321, "case_name": "Case 2"},
            {"x": 120, "expected": 21, "case_name": "Case 3"},
            {"x": 1534236469, "expected": 0, "case_name": "Case 4"}
        ],
        "sample_input": "x = 123",
        "sample_output": "321",
        "skeleton_code": {
            "python": """
class Solution:
    def reverse(self, x: int) -> int:
        # Write your code here
""",
            "javascript": """
class Solution {
    reverse(x) {
        // Write your code here
    }
}
""",
            "java": """
public class Main {
    public int reverse(int x) {
        // Write your code here
    }
}
"""
        },
        "wrapper_templates": {
            "python": """
class Solution:
    def reverse(self, x: int) -> int:
        {user_code}

# Wrapper code to handle I/O
if __name__ == "__main__":
    x = int(input())
    solution = Solution()
    result = solution.reverse(x)
    print(result)
""",
            "javascript": """
class Solution {
    reverse(x) {
        {user_code}
    }
}

process.stdin.on('data', data => {
    const x = parseInt(data.toString().trim());
    const solution = new Solution();
    const result = solution.reverse(x);
    console.log(result);
    process.exit();
});
""",
            "java": """
import java.util.Scanner;

public class Main {
    public int reverse(int x) {
        {user_code}
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        Main solution = new Main();
        int result = solution.reverse(x);
        System.out.println(result);
        sc.close();
    }
}
"""
        }
    },
    3: {
        "title": "Palindrome Check",
        "description": "Given a string `s`, return `true` if it is a palindrome, otherwise return `false`. A palindrome is a string that reads the same backward as forward.",
        "test_cases": [
            {"s": "racecar", "expected": True, "case_name": "Case 1"},
            {"s": "hello", "expected": False, "case_name": "Case 2"},
            {"s": "A man, a plan, a canal: Panama", "expected": True, "case_name": "Case 3"}
        ],
        "sample_input": "s = 'racecar'",
        "sample_output": "True",
        "skeleton_code": {
            "python": """
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Write your code here
""",
            "javascript": """
class Solution {
    isPalindrome(s) {
        // Write your code here
    }
}
""",
            "java": """
public class Main {
    public boolean isPalindrome(String s) {
        // Write your code here
    }
}
"""
        },
        "wrapper_templates": {
            "python": """
class Solution:
    def isPalindrome(self, s: str) -> bool:
        {user_code}

# Wrapper code to handle I/O
if __name__ == "__main__":
    s = input().strip()
    solution = Solution()
    result = solution.isPalindrome(s)
    print(result)
""",
            "javascript": """
class Solution {
    isPalindrome(s) {
        {user_code}
    }
}

process.stdin.on('data', data => {
    const s = data.toString().trim();
    const solution = new Solution();
    const result = solution.isPalindrome(s);
    console.log(result);
    process.exit();
});
""",
            "java": """
import java.util.Scanner;

public class Main {
    public boolean isPalindrome(String s) {
        {user_code}
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim();
        Main solution = new Main();
        boolean result = solution.isPalindrome(s);
        System.out.println(result);
        sc.close();
    }
}
"""
        }
    }
}

# Language configurations
LANGUAGES = {
    "python": {"ext": ".py", "cmd": ["python"], "setup": None},
    "javascript": {"ext": ".js", "cmd": ["node"], "setup": None},
    "java": {
        "ext": ".java", 
        "cmd": ["java", "Main"], 
        "setup": lambda f: subprocess.run(["javac", f], capture_output=True)
    }
}

@app.route('/')
def home():
    return render_template('index.html', challenges=CHALLENGES)

@app.route('/submit', methods=['POST'])
def submit_code():
    try:
        data = request.json
        challenge_id = int(data['challenge_id'])
        code = data['code']
        language = data['language']

        if challenge_id not in CHALLENGES or language not in LANGUAGES:
            return jsonify({"error": "Invalid challenge or language"}), 400

        # Get wrapper template and skeleton for the selected language
        challenge = CHALLENGES[challenge_id]
        wrapper_template = challenge["wrapper_templates"].get(language)
        skeleton = challenge["skeleton_code"].get(language)
        if not wrapper_template or not skeleton:
            return jsonify({"error": f"No wrapper template or skeleton for language: {language}"}), 400

        # Validate that the skeleton (function signature and class structure) is unchanged
        skeleton_lines = skeleton.strip().split("\n")
        code_lines = code.split("\n")
        skeleton_signature = "\n".join(line for line in skeleton_lines if not line.strip().startswith("#")).strip()
        code_signature = "\n".join(code_lines[:len(skeleton_lines) - 1]).strip()  # Exclude the comment line
        if code_signature != skeleton_signature:
            return jsonify({"error": "Do not modify the function signature or class structure."}), 400

        # Extract the user's logic (everything after the skeleton, excluding the comment)
        user_logic_start = len(skeleton_lines)
        for i, line in enumerate(code_lines):
            if line.strip().startswith("# Write your code here"):
                user_logic_start = i + 1
                break
        user_logic_lines = code_lines[user_logic_start:]
        
        # Normalize indentation (convert tabs to spaces, ensure 4-space indents)
        normalized_logic_lines = []
        for line in user_logic_lines:
            # Replace tabs with 4 spaces
            line = line.replace('\t', '    ')
            # Count leading spaces to determine indentation level
            leading_spaces = len(line) - len(line.lstrip(' '))
            # Normalize to 4-space indents
            indent_level = leading_spaces // 4
            normalized_line = '    ' * indent_level + line.lstrip(' ')
            normalized_logic_lines.append(normalized_line)
        user_logic = "\n".join(normalized_logic_lines).strip()
        if not user_logic:
            return jsonify({"error": "No logic provided. Please write your solution."}), 400

        # Use the normalized user logic directly
        full_code = wrapper_template.format(user_code=user_logic)

        # Prepare filename
        lang_config = LANGUAGES[language]
        timestamp = datetime.now().timestamp()
        filename = f"temp_{timestamp}{lang_config['ext']}"
        
        # Write full code to file
        with open(filename, 'w') as f:
            f.write(full_code)

        # Compile if needed (e.g., Java)
        if lang_config['setup']:
            compile_result = lang_config['setup'](filename)
            if compile_result.returncode != 0:
                os.remove(filename)
                return jsonify({"error": f"Compilation failed: {compile_result.stderr.decode()}"}), 400

        # Evaluate against predefined test cases
        results = []
        for test in challenge["test_cases"]:
            # Prepare input as two lines: nums array (JSON) and target
            test_input = f"{json.dumps(test['nums'])}\n{test['target']}" if challenge_id == 1 else str(test['x']) if challenge_id == 2 else test['s']
            try:
                start_time = time.time()
                process = subprocess.run(
                    lang_config['cmd'] + ([filename] if language != "java" else []),
                    input=test_input,
                    text=True,
                    capture_output=True,
                    timeout=2
                )
                execution_time = time.time() - start_time

                output = process.stdout.strip()
                expected = test["expected"]
                passed = False

                if challenge_id == 1:
                    passed = output == json.dumps(expected)
                elif challenge_id == 2:
                    passed = int(output) == expected
                elif challenge_id == 3:
                    passed = output.lower() == str(expected).lower()
                
                results.append({
                    "case_name": test["case_name"],
                    "input": test_input,
                    "expected": expected,
                    "got": output,
                    "passed": passed,
                    "execution_time": f"{execution_time:.3f}s",
                    "error": process.stderr.strip() if process.stderr else None
                })
            except subprocess.TimeoutExpired:
                results.append({"case_name": test["case_name"], "error": "Time Limit Exceeded (2s)"})
                break
            except Exception as e:
                results.append({"case_name": test["case_name"], "error": str(e)})
                break

        # Cleanup
        if os.path.exists(filename):
            os.remove(filename)
        if language == "java" and os.path.exists("Main.class"):
            os.remove("Main.class")

        # Calculate metrics
        total_tests = len(results)
        passed_tests = sum(1 for r in results if r.get("passed", False))
        
        return jsonify({
            "results": results,
            "score": (passed_tests / total_tests) * 100 if total_tests > 0 else 0,
            "total_tests": total_tests,
            "passed_tests": passed_tests
        })

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)