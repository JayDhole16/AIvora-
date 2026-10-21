import asyncio
import sys
from uuid import UUID
from app.services.database_service import DatabaseService
from app.services.embedding_service import EmbeddingService
from app.services.kb_service import KBService

AIVORA_KB_TEXT = """# AIVORA — BUSINESS KNOWLEDGE BASE

## 1. Business Overview
Business Name: Aivora
Business Type: AI Receptionist & Business Automation Platform
Description:
Aivora is an AI-powered receptionist and business automation platform designed for small and medium-sized businesses. It helps businesses handle customer conversations through voice calls, WhatsApp, and websites using AI.
Aivora can answer customer questions, provide business information, handle bookings, retrieve information from the business knowledge base, and escalate conversations to a human when required.
Primary Value:
Aivora helps businesses automate repetitive customer communication while allowing customers to interact with the business naturally.

## 2. Aivora Services

### AI Voice Receptionist
Aivora provides an AI voice receptionist that can answer incoming customer calls.
The AI receptionist can:
* Answer customer calls
* Greet customers
* Answer questions about the business
* Explain services
* Provide pricing information
* Answer FAQs
* Collect customer information
* Help customers book appointments
* Check availability when connected to the booking system
* Handle rescheduling and cancellation requests
* Transfer or escalate conversations to a human
* Operate according to configured business hours
* Handle after-hours behavior according to the business configuration
The voice receptionist can be configured with a specific persona, greeting, tone, voice, business hours, escalation number, and calendar.

### AI Website Receptionist
Aivora can provide an AI-powered receptionist on a business website.
Website visitors can use the AI to:
* Ask questions
* Learn about services
* Get pricing information
* Read FAQs
* Request appointments
* Get business information
* Be connected to a human when necessary
The website receptionist uses the same business knowledge base as the other Aivora channels.

### WhatsApp AI Receptionist
Aivora can provide an AI receptionist through WhatsApp.
Customers can use WhatsApp to:
* Ask questions
* Learn about services
* Get pricing information
* Ask about business hours
* Request appointments
* Reschedule appointments
* Cancel appointments
* Receive relevant business information
* Request human assistance
The WhatsApp receptionist uses the business's configured knowledge base.

## 3. Knowledge Base
Each business using Aivora can create its own knowledge base.
The knowledge base can contain information such as:
* Business information
* Services
* Pricing
* Business hours
* FAQs
* Policies
* Booking information
* Custom information
Businesses can also upload documents such as:
* Price lists
* Menus
* Brochures
* Other business documents
Uploaded documents can be processed into structured knowledge-base information.
The knowledge base is shared across Aivora's supported customer communication channels.

## 4. Booking System
Aivora can connect the AI receptionist to a booking or calendar system.
When a customer wants to book an appointment, the AI should:
1. Understand what the customer wants to book.
2. Collect the required customer information.
3. Check real-time availability using the booking system.
4. Present available times to the customer.
5. Allow the customer to select a suitable time.
6. Confirm the booking.
7. Provide the customer with the booking details.
Aivora can also support requests to reschedule or cancel appointments when the relevant booking integration is available.
The AI must not claim that an appointment is available unless availability has actually been checked.

## 5. Human Handoff
Aivora supports escalation from the AI receptionist to a human.
The AI should offer or perform human escalation when:
* The customer explicitly asks to speak to a human.
* The customer has a complaint.
* The customer is angry or highly dissatisfied.
* The customer has a complicated request.
* The customer asks for information that is not available in the knowledge base.
* The request requires a human decision.
* There is a payment, refund, or other sensitive issue requiring human assistance.
The business can configure an escalation phone number for the voice receptionist.

## 6. Voice Receptionist Configuration
Aivora's voice receptionist can be configured with:
* AI persona
* Greeting
* Voice
* Tone
* Business hours
* After-hours behavior
* Phone number
* Calendar integration
* Escalation number
* Advanced voice settings
The business owner can test the receptionist before making it live.

## 7. Business Hours
Business hours are configured separately for each business.
The AI receptionist should use the configured business hours when deciding how to handle calls.
During business hours:
The AI can handle customer conversations normally.
Outside business hours:
The AI should follow the business's configured after-hours behavior.
The AI must not invent business hours if they have not been configured.

## 8. Pricing
Aivora pricing depends on the configuration and services selected by the business.
Potential factors may include:
* AI receptionist services
* Voice usage
* WhatsApp integration
* Website receptionist
* Booking integrations
* Phone number costs
* Third-party service costs
* Other configured features
If an exact Aivora price is not available in the knowledge base, the receptionist must not invent a price.
Instead, it should explain that pricing depends on the business's requirements and offer to connect the customer with the Aivora team.

## 9. Frequently Asked Questions

### What is Aivora?
Aivora is an AI receptionist and business automation platform that helps businesses handle customer conversations through voice, WhatsApp, and websites.

### Can Aivora answer phone calls?
Yes. Aivora can provide an AI voice receptionist that answers incoming customer calls and handles common customer requests.

### Can the AI receptionist answer questions about my business?
Yes. The receptionist uses the business's knowledge base to answer questions about services, pricing, hours, FAQs, and other configured information.

### Can Aivora book appointments?
Yes. When connected to a compatible booking or calendar system, Aivora can check availability and help customers book appointments.

### Can customers talk to a human?
Yes. Aivora supports human escalation when a customer requests it or when the AI determines that human assistance is required.

### Can I customize the AI receptionist?
Yes. The voice receptionist can be configured with a persona, greeting, voice, tone, business hours, escalation settings, and other settings.

### Can I test the AI receptionist before going live?
Yes. Aivora provides a test-call experience so the business can test the receptionist before deployment.

### Can I upload my business documents?
Yes. Businesses can upload documents such as price lists, menus, and brochures to help populate their knowledge base.

### Does Aivora support WhatsApp?
Yes. Aivora is designed to support WhatsApp as one of its customer communication channels.

### Does Aivora work on websites?
Yes. Aivora can provide an AI receptionist experience for business websites.

### Can the AI make up information?
No. The AI receptionist must only provide information supported by the business knowledge base or verified tools.

### What happens when the AI does not know something?
The AI should clearly state that it does not have the required information and offer to connect the customer with a human representative.

## 10. Information Accuracy Rules
The AI receptionist must treat the configured Aivora knowledge base as the source of truth for business-specific information.
The AI must:
* Never invent prices.
* Never invent services.
* Never invent business hours.
* Never invent policies.
* Never claim an appointment is available without checking availability.
* Never claim a booking was completed unless the booking system confirms it.
* Never provide unsupported information as fact.
* Ask for clarification when the customer's request is unclear.
* Escalate to a human when necessary.
If information is unavailable, the AI should say:
"I'm not completely sure about that. I can connect you with someone from the Aivora team who can help."

## 11. Customer Information
Depending on the requested action, the AI may need to collect information such as:
* Customer name
* Phone number
* Requested service
* Preferred date
* Preferred time
* Other information required by the business
The AI should only collect information necessary to complete the customer's request.

## 12. Example Customer Questions
Customers may ask:
"What is Aivora?"
"What does Aivora do?"
"Can Aivora answer my business calls?"
"Can I use Aivora on WhatsApp?"
"Can Aivora be added to my website?"
"Can your AI receptionist book appointments?"
"Can I customize the AI voice?"
"Can I upload my business information?"
"How does the AI know about my business?"
"Can I test the receptionist before going live?"
"What happens if the AI doesn't know the answer?"
"Can I transfer a customer to my employee?"
"Does Aivora support business hours?"
"Can the receptionist work after business hours?"
"Can I connect my calendar?"
"How does Aivora handle bookings?"
"How much does Aivora cost?"
"What integrations do you support?"

## 13. Important Limitation
Aivora's AI receptionist should not promise functionality that has not been configured or integrated for a particular business.
For example:
If a calendar is not connected, the AI should not claim that it can check real-time availability.
If a phone number has not been configured, the AI should not claim that a dedicated number has already been provisioned.
If a specific integration is unavailable, the AI should not claim that it is supported.

## 14. Primary Objective
The primary objective of Aivora is to help businesses automate customer communication while maintaining accurate, useful, and natural interactions.
The AI receptionist should resolve customer requests whenever possible and escalate to a human whenever the request requires human intervention.
"""

async def main():
    if len(sys.argv) < 2:
        print("Usage: python add_kb.py <org_id>")
        print("Example: python add_kb.py 5903abf4-0274-4816-b9d5-6285c70d9f17")
        sys.exit(1)
    
    org_id = UUID(sys.argv[1])
    
    db_service = DatabaseService()
    embedding_service = EmbeddingService()
    kb_service = KBService(db_service, embedding_service)
    
    print(f"Adding Aivora knowledge base to org {org_id}...")
    result = await kb_service.parse_text(org_id, AIVORA_KB_TEXT)
    
    if result.get("success"):
        print(f"✓ Successfully added {result.get('entries_created', 0)} KB entries")
        for entry in result.get("entries", []):
            print(f"  - {entry['title']}")
    else:
        print(f"✗ Error: {result.get('error', 'Unknown error')}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
