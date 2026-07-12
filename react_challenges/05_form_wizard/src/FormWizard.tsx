// TODO: Implement the FormWizard component.
//
// This file contains the type definitions and a component stub.
// Read CHALLENGE.md for the full requirements.

export interface PersonalInfo {
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
}

export interface AddressInfo {
  street: string;
  city: string;
  state: string;
  zip: string;
  country: string;
}

export type WizardFormData = PersonalInfo & AddressInfo;

export type WizardStep = 1 | 2 | 3;

export interface ValidationErrors {
  [field: string]: string;
}

// ---------------------------------------------------------------------------
// FormWizard component
// ---------------------------------------------------------------------------
// Requirements summary (see CHALLENGE.md for the complete spec):
//
//  - Three-step wizard:
//      Step 1 – Personal Info  (firstName, lastName, email, phone)
//      Step 2 – Address        (street, city, state, zip, country)
//      Step 3 – Review + Submit (read-only summary, then submit)
//
//  - Step indicator at the top showing step number + label, with the current
//    step highlighted.
//
//  - "Next" validates the current step before advancing.
//    "Back" returns to the previous step, preserving all entered data.
//
//  - Validation rules:
//      firstName, lastName : required, min 2 characters
//      email               : required, valid e-mail format
//      phone               : optional; if provided must match a phone pattern
//      street, city, zip   : required
//      state               : required
//      country             : required
//
//  - On submit, call `submitFormData(data)` from `./mockApi`.
//    Show a loading indicator while the request is in-flight.
//    Show a success screen (with confirmation number) or error screen after.
//    The error screen should allow retrying the submit.
//    Both screens should include a "Start Over" button that resets to step 1.
//
//  - Accessible: every <input> must have a corresponding <label>.
//    Validation error messages must be linked to their input via
//    `aria-describedby`.
//
//  - State management: use useState or useReducer only — no form libraries.
// ---------------------------------------------------------------------------

export default function FormWizard() {
  // TODO: implement
  return (
    <div>
      <p>FormWizard not yet implemented. See CHALLENGE.md for instructions.</p>
    </div>
  );
}
