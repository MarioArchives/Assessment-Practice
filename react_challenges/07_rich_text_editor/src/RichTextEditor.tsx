export interface RichTextEditorProps {
  value: string;
  onChange: (html: string) => void;
  placeholder?: string;
  readOnly?: boolean;
  minHeight?: number; // px, default 150
  maxHeight?: number; // px, optional
}

type FormatCommand = 'bold' | 'italic' | 'insertUnorderedList';

interface ToolbarState {
  bold: boolean;
  italic: boolean;
  unorderedList: boolean;
}

// TODO: implement
export default function RichTextEditor(_props: RichTextEditorProps) {
  return (
    <div>
      {/* TODO: implement RichTextEditor */}
    </div>
  );
}
