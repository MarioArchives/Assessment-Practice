export interface PaymentData {
  cardNumber: string;
  expiry: string;
  cvv: string;
  nameOnCard: string;
}

export interface PaymentResult {
  success: boolean;
  orderNumber?: string;
  error?: string;
}

function generateOrderNumber(): string {
  const digits = Math.floor(100000 + Math.random() * 900000).toString();
  return `ORD-2024-${digits}`;
}

function randomDelay(): Promise<void> {
  const ms = 1500 + Math.random() * 1000; // 1500–2500ms
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Simulates payment processing; 1500-2500ms delay; 20% failure rate
export async function processPayment(data: PaymentData): Promise<PaymentResult> {
  // Suppress unused-parameter warning — data would be sent to a real API
  void data;

  await randomDelay();

  const failed = Math.random() < 0.2;

  if (failed) {
    return {
      success: false,
      error: 'Your card was declined. Please check your details and try again.',
    };
  }

  return {
    success: true,
    orderNumber: generateOrderNumber(),
  };
}
