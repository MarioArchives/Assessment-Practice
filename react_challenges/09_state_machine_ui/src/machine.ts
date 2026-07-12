import { useState } from 'react';

// The state machine definition and hook

export type CheckoutState =
  | 'cart'
  | 'shipping'
  | 'payment'
  | 'confirming'
  | 'confirmed'
  | 'failed';

export type CheckoutEvent =
  | 'PROCEED'
  | 'BACK'
  | 'SUBMIT_SHIPPING'
  | 'SUBMIT_PAYMENT'
  | 'PAYMENT_SUCCESS'
  | 'PAYMENT_FAILURE'
  | 'RETRY'
  | 'RESTART';

export type StateMachine<S extends string, E extends string> = {
  [state in S]?: Partial<Record<E, S>>;
};

// TODO: define checkoutMachine object here
export const checkoutMachine: StateMachine<CheckoutState, CheckoutEvent> = {
  // TODO: implement transitions
};

// TODO: implement useMachine hook
export function useMachine<S extends string, E extends string>(
  machine: StateMachine<S, E>,
  initialState: S
): [S, (event: E) => void] {
  // TODO: implement
  void machine;
  void initialState;
  throw new Error('Not implemented');
}
