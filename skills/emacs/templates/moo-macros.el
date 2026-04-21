;;; moo-macros.el — keyboard macros and schema export hooks

(defun moo-save-last-macro (name)
  "Name `last-kbd-macro' as NAME."
  (interactive "sMacro name: ")
  (name-last-kbd-macro name))

(defun moo-extract-schemas ()
  "Placeholder: collect macro / oneshot paths for review."
  (interactive)
  (message "moo-extract-schemas: hook your review buffer here"))

(provide 'moo-macros)
