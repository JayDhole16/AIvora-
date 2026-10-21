from app.db.supabase import get_supabase_client

client = get_supabase_client()

# First, let's list all organizations
print("Fetching organizations...")
result = client.table('organizations').select('id, name').execute()
if result.data:
    print(f"Found {len(result.data)} organizations:")
    for org in result.data:
        print(f"  ID: {org['id']}")
        print(f"  Name: {org.get('name', 'N/A')}")
        print()
else:
    print("No organizations found")
