import React from 'react';

// Context
interface TabsContextValue {
  activeValue: string;
  setActiveValue: (value: string) => void;
  baseId: string;
}

const TabsContext = React.createContext<TabsContextValue | null>(null);

function useTabsContext(): TabsContextValue {
  const ctx = React.useContext(TabsContext);
  if (!ctx) throw new Error('Tabs compound components must be used within <Tabs>');
  return ctx;
}

// Props interfaces
export interface TabsProps {
  defaultValue?: string;
  value?: string;
  onChange?: (value: string) => void;
  children: React.ReactNode;
}

export interface TabsListProps {
  children: React.ReactNode;
  'aria-label'?: string;
}

export interface TabProps {
  value: string;
  children: React.ReactNode;
  disabled?: boolean;
}

export interface TabsPanelsProps {
  children: React.ReactNode;
}

export interface TabPanelProps {
  value: string;
  children: React.ReactNode;
}

// Component stubs
function TabsRoot(_props: TabsProps): React.ReactElement {
  // TODO: implement - manage controlled/uncontrolled state, provide context
  return <div>{/* TODO */}</div>;
}

function TabsList(_props: TabsListProps): React.ReactElement {
  // TODO: implement - render tablist with keyboard navigation
  return <div>{/* TODO */}</div>;
}

function Tab(_props: TabProps): React.ReactElement {
  // TODO: implement - render tab button with ARIA, read context
  return <button type="button">{/* TODO */}</button>;
}

function TabsPanels(_props: TabsPanelsProps): React.ReactElement {
  // TODO: implement
  return <div>{/* TODO */}</div>;
}

function TabPanel(_props: TabPanelProps): React.ReactElement {
  // TODO: implement - render panel, hidden when not active
  return <div>{/* TODO */}</div>;
}

// Compound component assembly
const Tabs = Object.assign(TabsRoot, {
  List: TabsList,
  Tab: Tab,
  Panels: TabsPanels,
  Panel: TabPanel,
});

export default Tabs;
