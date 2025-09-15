def generate_report(email, check_results):
    print("\n=== Email Summary ===")
    print(f"From: {email.get('from', 'N/A')}")
    print(f"Subject: {email.get('subject', 'N/A')}")

    issues = []
    for result in check_results:
        # If it's a tuple/list
        if isinstance(result, (tuple, list)):
            flag = result[0]
            info = result[1] if len(result) > 1 else None
            if flag and info:
                issues.append(info)

        # If it's a dict
        elif isinstance(result, dict):
            if result.get("flag") and "info" in result:
                issues.append(result["info"])

    if issues:
        print("\n⚠️ Suspicious Indicators Found:")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
    else:
        print("\n✅ No obvious suspicious indicators found.")
