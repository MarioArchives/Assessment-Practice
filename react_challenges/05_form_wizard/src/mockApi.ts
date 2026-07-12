export interface FormData {
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  street: string;
  city: string;
  state: string;
  zip: string;
  country: string;
}

export interface SubmitResult {
  success: boolean;
  confirmationNumber?: string;
  error?: string;
}

/**
 * Simulates a POST request to a remote API.
 * - Resolves after a random delay between 1000–1500ms.
 * - Has a 10% chance of simulating a server-side failure so that
 *   candidates can verify their error-handling path.
 */
export async function submitFormData(data: FormData): Promise<SubmitResult> {
  // Simulate network latency: 1000–1500ms
  const delay = 1000 + Math.random() * 500;
  await new Promise((resolve) => setTimeout(resolve, delay));

  // 10% random failure
  if (Math.random() < 0.1) {
    return {
      success: false,
      error: 'An unexpected server error occurred. Please try again.',
    };
  }

  // Generate a confirmation number like CONF-A3F9K2
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  const confirmationNumber =
    'CONF-' +
    Array.from({ length: 6 }, () =>
      chars.charAt(Math.floor(Math.random() * chars.length))
    ).join('');

  console.log('Form submitted successfully:', data);

  return {
    success: true,
    confirmationNumber,
  };
}
