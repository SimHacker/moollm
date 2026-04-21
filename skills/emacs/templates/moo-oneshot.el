;;; moo-oneshot.el — one-shot functions and promotion (play-learn-lift)

(defvar moo-oneshot-log-file
  (expand-file-name "oneshot-log.el" (expand-file-name "lib" (expand-file-name "moo" user-emacs-directory))))

(defun moo-define-oneshot (name body)
  "Append a defun stub for NAME to the oneshot log."
  (interactive "sName:\nsBody: ")
  (make-directory (file-name-directory moo-oneshot-log-file) t)
  (with-temp-buffer
    (insert (format ";; oneshot %S\n(defun %s ()\n  %s)\n" name name body))
    (append-to-file (point-min) (point-max) moo-oneshot-log-file)))

(provide 'moo-oneshot)
