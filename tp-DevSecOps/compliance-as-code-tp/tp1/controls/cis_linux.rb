control 'cis-5.2.4' do
  impact 1.0
  title 'Ensure SSH PermitRootLogin is disabled'

  describe sshd_config do
    its('PermitRootLogin') { should cmp 'no' }
  end
end

control 'cis-5.2.11' do
  impact 0.7
  title 'Ensure SSH MaxAuthTries is set to 4 or less'

  describe sshd_config do
    its('MaxAuthTries') { should cmp <= 4 }
  end
end

control 'cis-1.1.1' do
  impact 0.5
  title 'Ensure /tmp is configured'

  describe mount('/tmp') do
    it { should be_mounted }
  end
end
