import React from 'react'

export interface ColumnDef<T> {
  key: keyof T & string
  header: string
  sortable?: boolean
  render?: (value: T[keyof T], row: T) => React.ReactNode
}

export interface DataTableProps<T extends Record<string, unknown>> {
  columns: ColumnDef<T>[]
  rows: T[]
  pageSize?: number
}

type SortDirection = 'asc' | 'desc' | 'none'

interface SortState {
  key: string
  direction: SortDirection
}

// TODO: implement
export default function DataTable<T extends Record<string, unknown>>(
  _props: DataTableProps<T>,
): React.ReactElement | null {
  return null
}
