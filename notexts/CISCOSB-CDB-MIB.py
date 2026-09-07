#
# PySNMP MIB module CISCOSB-CDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-CDB-MIB
# Source digest sha256:d7f4dc2fb5fc4195b0d77b7a11b71c114385cb7effba045bc6441eec82049655
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
rlCDB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94))
rlCDB.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlCDB.setLastUpdated('2007-01-02 00:00')
if mibBuilder.loadTexts: rlCDB.setOrganization('Cisco Systems, Inc.')
rlStartupCDBChanged = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBChanged.setStatus('current')
rlManualReboot = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlManualReboot.setStatus('current')
rlStartupCDBEmpty = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 94, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBEmpty.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-CDB-MIB", PYSNMP_MODULE_ID=rlCDB, rlCDB=rlCDB, rlManualReboot=rlManualReboot, rlStartupCDBChanged=rlStartupCDBChanged, rlStartupCDBEmpty=rlStartupCDBEmpty)
