import { useRef, useState } from "react"
import { isFocused } from "./utils"

export interface AutocompleteProps {
  /** The full list of options to filter. */
  data: string[]
  /** Called with the selected value whenever the user makes a selection. */
  onSelect?: (value: string) => void
  /** Placeholder text for the input element. */
  placeholder?: string
  /** Optional id prefix used to generate stable ARIA ids. */
  id?: string
}

/**
 * TODO: implement an accessible autocomplete / combobox component.
 *
 * Requirements summary:
 *  - Filter `data` case-insensitively as the user types
 *  - Show a dropdown list of matches below the input
 *  - Support ArrowUp / ArrowDown to move the highlighted option
 *  - Enter selects the highlighted option; Escape closes the dropdown
 *  - Clicking an option selects it
 *  - Click-outside closes the dropdown
 *  - Mark the active option via aria-activedescendant on the input
 *  - Use role="combobox", role="listbox", role="option" ARIA roles
 *  - aria-expanded reflects the open/closed state of the dropdown
 *  - Show "No results" when no options match the current input
 *
 * See CHALLENGE.md for the full specification, constraints, hints, and
 * evaluation criteria.
 */
export default function Autocomplete(_props: AutocompleteProps) {
  const [suggestions, setSuggestions] = useState<string[]>(_props.data)
  const [isOpen, setIsOpen] = useState<boolean>(false)
  const componentRef = useRef(null)
  const hanldeClick = (newSelection: string) => {
    if (_props.onSelect) {
      _props.onSelect(newSelection)
    }
  }
  const handleValueUpdate = (newValue: string) => {
    let updatedSuggestions: string[] = _props.data.filter(entry => entry.toLowerCase().includes(newValue.toLowerCase()))
    if (!updatedSuggestions.length) {
      updatedSuggestions = ["no results"]
    }
    setSuggestions(updatedSuggestions)
  }
  const handleDropdownOpen = (keyPressed: string) => {

    if (keyPressed === "Enter") {
      setIsOpen(true)
    }
    if (!isFocused(document.activeElement, componentRef.current)) {
      setIsOpen(false)
    }

  }

  return (
    <div>
      <input ref={componentRef} className="autocomplete" type="text" onChange={(e) => handleValueUpdate(e.target.value)} onKeyDown={(e) => handleDropdownOpen(e.key)} />
      <ul>
        {isOpen ?
          suggestions.map((entry) =>
          (<li key={entry} onClick={() => hanldeClick(entry)}>{entry}</li>
          )) : <></>
        }
      </ul>
    </div>
  )
}
