"""Human-in-the-Loop Interceptor"""

def check_permission(tool_name, is_automated=True):
    high_risk = {"delete_database", "send_wire_transfer", "deploy_production"}
    if tool_name in high_risk and not is_automated:
        return False, "BLOCKED: Requires human manual confirmation"
    return True, "APPROVED: Operation permitted"

if __name__ == "__main__":
    print("[RUN] Human-in-the-Loop Guardrail...")
    ok, msg = check_permission("delete_database", is_automated=False)
    print(f"[OK] Policy Check: {msg}")
