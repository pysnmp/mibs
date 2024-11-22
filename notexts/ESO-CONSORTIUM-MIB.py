#
# PySNMP MIB module ESO-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eso/ESO-CONSORTIUM-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 11:55:04 2024
# On host fv-az665-602 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, iso, MibIdentifier, NotificationType, Unsigned32, ObjectIdentity, Bits, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, snmpModules, Counter32, Gauge32, Integer32, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "iso", "MibIdentifier", "NotificationType", "Unsigned32", "ObjectIdentity", "Bits", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "snmpModules", "Counter32", "Gauge32", "Integer32", "TimeTicks", "ModuleIdentity")
AutonomousType, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ESO-CONSORTIUM-MIB", usm3DESPrivProtocol=usm3DESPrivProtocol, esoConsortiumMIBObjectIdentities=esoConsortiumMIBObjectIdentities, esoConsortiumMIB=esoConsortiumMIB, usmAESCfb256PrivProtocol=usmAESCfb256PrivProtocol, usmAESCfb192PrivProtocol=usmAESCfb192PrivProtocol, PYSNMP_MODULE_ID=esoConsortiumMIB, usmAESCfb128PrivProtocol=usmAESCfb128PrivProtocol)
