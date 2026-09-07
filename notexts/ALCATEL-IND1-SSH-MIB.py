#
# PySNMP MIB module ALCATEL-IND1-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source ALCATEL-IND1-SSH-MIB
# Source digest sha256:62676a0c8b1e2e4957615731eb1fde56105494ac576ad29a19b7e4e35397391f
# Produced by pysmi-2.3.0
#
softentIND1Ssh, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Ssh")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1SshMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1))
alcatelIND1SshMIB.setRevisions(('2019-10-07 00:00',))
if mibBuilder.loadTexts: alcatelIND1SshMIB.setLastUpdated('2019-10-07 00:00')
if mibBuilder.loadTexts: alcatelIND1SshMIB.setOrganization('ALE USA Inc')
alcatelIND1SshMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 1))
if mibBuilder.loadTexts: alcatelIND1SshMIBObjects.setStatus('current')
alcatelIND1SshMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 2))
if mibBuilder.loadTexts: alcatelIND1SshMIBConformance.setStatus('current')
alcatelIND1SshMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1SshMIBGroups.setStatus('current')
alcatelIND1SshMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1SshMIBCompliances.setStatus('current')
alaSshAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSshAdminStatus.setStatus('current')
alaScpSftpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaScpSftpAdminStatus.setStatus('current')
alaSshPubKeyEnforceAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSshPubKeyEnforceAdminStatus.setStatus('current')
alaSshPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSshPortNumber.setStatus('current')
alcatelIND1SshMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-SSH-MIB", "alaSshConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1SshMIBCompliance = alcatelIND1SshMIBCompliance.setStatus('current')
alaSshConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-SSH-MIB", "alaSshAdminStatus"), ("ALCATEL-IND1-SSH-MIB", "alaScpSftpAdminStatus"), ("ALCATEL-IND1-SSH-MIB", "alaSshPubKeyEnforceAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaSshConfigGroup = alaSshConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-SSH-MIB", PYSNMP_MODULE_ID=alcatelIND1SshMIB, alaScpSftpAdminStatus=alaScpSftpAdminStatus, alaSshAdminStatus=alaSshAdminStatus, alaSshConfigGroup=alaSshConfigGroup, alaSshPortNumber=alaSshPortNumber, alaSshPubKeyEnforceAdminStatus=alaSshPubKeyEnforceAdminStatus, alcatelIND1SshMIB=alcatelIND1SshMIB, alcatelIND1SshMIBCompliance=alcatelIND1SshMIBCompliance, alcatelIND1SshMIBCompliances=alcatelIND1SshMIBCompliances, alcatelIND1SshMIBConformance=alcatelIND1SshMIBConformance, alcatelIND1SshMIBGroups=alcatelIND1SshMIBGroups, alcatelIND1SshMIBObjects=alcatelIND1SshMIBObjects)
