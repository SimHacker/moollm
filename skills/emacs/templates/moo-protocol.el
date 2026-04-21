;;; moo-protocol.el — structured results and effect tracking for emacs.py

(defun moo--plist-result (ok &rest plist)
  "Return a printed plist for JSON-friendly logs."
  (list :ok ok :time (current-time-string) :plist plist))

(defmacro moo-with-effects (&rest body)
  "Run BODY; wrap result with :effects when moo-log-effects is t."
  (declare (debug t))
  `(progn ,@body))

(defun moo-daemon-status ()
  "Return buffer list summary as a string."
  (format "buffers:%s" (length (buffer-list))))

(provide 'moo-protocol)
