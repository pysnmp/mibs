#
# PySNMP MIB module RITTAL-CMC-III-CAPABILITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rittal/RITTAL-CMC-III-CAPABILITY-MIB
# Produced by pysmi-1.1.12 at Tue Jun 18 02:39:16 2024
# On host fv-az849-858 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
cmcIII, = mibBuilder.importSymbols("RITTAL-CMC-III-MIB", "cmcIII")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, Integer32, Counter64, TimeTicks, ModuleIdentity, MibIdentifier, Bits, Counter32, ObjectIdentity, NotificationType, Unsigned32, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Counter64", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Bits", "Counter32", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmcIIICapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 2606, 7, 8))
cmcIIICapability.setRevisions(('2015-10-27 00:00', '2014-10-06 00:00', '2013-03-30 00:00', '2012-08-30 00:00', '2011-09-01 00:00',))
if mibBuilder.loadTexts: cmcIIICapability.setLastUpdated('201510270000Z')
if mibBuilder.loadTexts: cmcIIICapability.setOrganization('RITTAL GmbH & Co. KG')
cmcIIIPuCapsV102 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2606, 7, 8, 30102))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV102 = cmcIIIPuCapsV102.setProductRelease('V1.02')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV102 = cmcIIIPuCapsV102.setStatus('current')
cmcIIIPuCapsV103 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2606, 7, 8, 30103))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV103 = cmcIIIPuCapsV103.setProductRelease('V1.03')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV103 = cmcIIIPuCapsV103.setStatus('current')
cmcIIIPuCapsV104 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2606, 7, 8, 30104))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV104 = cmcIIIPuCapsV104.setProductRelease('V1.04')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPuCapsV104 = cmcIIIPuCapsV104.setStatus('current')
cmcIIIPduCapsV104 = AgentCapabilities((1, 3, 6, 1, 4, 1, 2606, 7, 8, 34104))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPduCapsV104 = cmcIIIPduCapsV104.setProductRelease('V1.04')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmcIIIPduCapsV104 = cmcIIIPduCapsV104.setStatus('current')
mibBuilder.exportSymbols("RITTAL-CMC-III-CAPABILITY-MIB", cmcIIICapability=cmcIIICapability, PYSNMP_MODULE_ID=cmcIIICapability, cmcIIIPduCapsV104=cmcIIIPduCapsV104, cmcIIIPuCapsV102=cmcIIIPuCapsV102, cmcIIIPuCapsV104=cmcIIIPuCapsV104, cmcIIIPuCapsV103=cmcIIIPuCapsV103)
