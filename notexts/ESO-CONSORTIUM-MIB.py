#
# PySNMP MIB module ESO-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eso/ESO-CONSORTIUM-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 15:59:43 2024
# On host fv-az1245-338 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter32, iso, Bits, snmpModules, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter64, NotificationType, IpAddress, ObjectIdentity, ModuleIdentity, TimeTicks, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "iso", "Bits", "snmpModules", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter64", "NotificationType", "IpAddress", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "Unsigned32", "Integer32")
TextualConvention, AutonomousType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "AutonomousType", "DisplayString")
esoConsortiumMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14832))
esoConsortiumMIB.setRevisions(('2004-06-23 00:00', '2003-02-03 00:00', '2003-02-03 00:00',))
if mibBuilder.loadTexts: esoConsortiumMIB.setLastUpdated('200406230000Z')
if mibBuilder.loadTexts: esoConsortiumMIB.setOrganization('ESO (Extended Security Options) Consortium')
esoConsortiumMIBObjectIdentities = MibIdentifier((1, 3, 6, 1, 4, 1, 14832, 1))
usm3DESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 1))
if mibBuilder.loadTexts: usm3DESPrivProtocol.setStatus('current')
usmAESCfb128PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 2))
if mibBuilder.loadTexts: usmAESCfb128PrivProtocol.setStatus('deprecated')
usmAESCfb192PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 3))
if mibBuilder.loadTexts: usmAESCfb192PrivProtocol.setStatus('current')
usmAESCfb256PrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 4))
if mibBuilder.loadTexts: usmAESCfb256PrivProtocol.setStatus('current')
mibBuilder.exportSymbols("ESO-CONSORTIUM-MIB", usmAESCfb192PrivProtocol=usmAESCfb192PrivProtocol, esoConsortiumMIBObjectIdentities=esoConsortiumMIBObjectIdentities, esoConsortiumMIB=esoConsortiumMIB, usmAESCfb256PrivProtocol=usmAESCfb256PrivProtocol, usm3DESPrivProtocol=usm3DESPrivProtocol, usmAESCfb128PrivProtocol=usmAESCfb128PrivProtocol, PYSNMP_MODULE_ID=esoConsortiumMIB)
