;;; moo-structural.el — structural editing helpers

(defun moo-goto-defun (name)
  "Move point to defun named NAME (simple search)."
  (interactive "sDefun: ")
  (goto-char (point-min))
  (search-forward-regexp (concat "(defun\\s-+" (regexp-quote name) "\\b") nil t))

(defmacro moo-try (&rest body)
  "Execute BODY inside `atomic-change-group'."
  (declare (debug t))
  `(atomic-change-group (progn ,@body)))

(provide 'moo-structural)
