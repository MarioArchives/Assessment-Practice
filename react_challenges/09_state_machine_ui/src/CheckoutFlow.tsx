import type { CheckoutState } from './machine';

// Cart item for the demo
export interface CartItem {
  id: string;
  name: string;
  price: number;
  quantity: number;
}

export const DEMO_CART: CartItem[] = [
  { id: '1', name: 'Wireless Mechanical Keyboard', price: 149.99, quantity: 1 },
  { id: '2', name: 'USB-C Hub (7-in-1)', price: 49.99, quantity: 2 },
  { id: '3', name: 'Monitor Light Bar', price: 39.99, quantity: 1 },
];

// Suppress unused import warning until the component is implemented
void (null as unknown as CheckoutState);

// CheckoutFlow component - TODO: implement
export default function CheckoutFlow() {
  // TODO: implement using useMachine from './machine'
  return null;
}
