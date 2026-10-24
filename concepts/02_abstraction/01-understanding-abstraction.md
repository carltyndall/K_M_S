# Understanding Abstraction

Abstraction is the technique of hiding complex internal implementation details and exposing only the essential interface necessary to interact with a component.

---

## 🧠 Mental Model: The Automobile Interface
When driving a car, you interact with:
- The steering wheel (Interface)
- The accelerator pedal (Interface)
- The brake pedal (Interface)

You do not need to manually manage fuel injection, cylinder combustion, or hydraulic pressure to drive. The complex mechanical systems are **abstracted away**.

## 💻 Abstraction in Software
In programming, abstraction appears across multiple levels:
- **Functions:** Wrap a multi-step routine into a named callable unit (`def send_email():`).
- **Data Structures:** Present simple methods (`list.append()`) while managing memory buffers behind the scenes.
- **Modules & Packages:** Expose clear public APIs while keeping private helper routines encapsulated.
