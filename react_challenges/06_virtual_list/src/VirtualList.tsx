import React from 'react'

export interface VirtualListProps<T> {
  items: T[]
  itemHeight: number
  containerHeight: number
  renderItem: (item: T, index: number) => React.ReactNode
  overscan?: number
}

// VirtualList is a generic component
// TODO: implement
export default function VirtualList<T>(_props: VirtualListProps<T>): React.ReactElement | null {
  // TODO: implement
  return null
}
