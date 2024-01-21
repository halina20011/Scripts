local status_ok, _ = pcall(require, "lspconfig")
if not status_ok then
    return
end

require "User.lsp.mason"
require ("User.lsp.handlers").setup();
-- require "User.lsp.handlers";

require "User.lsp.nullLs"
