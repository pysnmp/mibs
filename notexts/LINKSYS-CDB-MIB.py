#
# PySNMP MIB module LINKSYS-CDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source LINKSYS-CDB-MIB
# Source digest sha256:1e679aa26c5cdefdd4fa775b27801f67f3409d30011e97551cd9888d33ebfca4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
rlCDB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 94))
rlCDB.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlCDB.setLastUpdated('2007-01-02 00:00')
if mibBuilder.loadTexts: rlCDB.setOrganization(' Linksys LLC.')
rlStartupCDBChanged = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 94, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBChanged.setStatus('current')
rlManualReboot = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 94, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlManualReboot.setStatus('current')
mibBuilder.exportSymbols("LINKSYS-CDB-MIB", PYSNMP_MODULE_ID=rlCDB, rlCDB=rlCDB, rlManualReboot=rlManualReboot, rlStartupCDBChanged=rlStartupCDBChanged)
